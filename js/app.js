/**
 * CDAC DBMS Master - Interactive Study Application Logic
 * Pair programmed with Database Lecturer & Senior Developer
 */

(function () {
  'use strict';

  // State Management
  const STORAGE_KEY = 'CDAC_DBMS_APP_STATE_V1';

  const defaultState = {
    theme: 'light',
    lang: 'bilingual', // 'vi', 'bilingual', 'en'
    currentTab: 'practice', // 'practice', 'flashcard', 'exam', 'bookmarks'
    selectedModule: 0, // 0 = all
    statusFilter: 'all', // 'all', 'unanswered', 'correct', 'wrong', 'bookmarked'
    searchQuery: '',
    answers: {}, // { [qId]: { selected: 'A', isCorrect: true } }
    bookmarks: [], // [qId]
    flashcardMastered: [], // [qId]
    flashcardIndex: 0,
    flashcardIsFlipped: false,
    exam: {
      inProgress: false,
      questions: [],
      userAnswers: {},
      timeRemaining: 0,
      totalTime: 0,
      submitted: false,
      score: 0
    }
  };

  let state = loadState();
  let timerInterval = null;

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        return { ...defaultState, ...JSON.parse(raw) };
      }
    } catch (e) {
      console.warn('Could not load state from localStorage:', e);
    }
    return { ...defaultState };
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn('Could not save state to localStorage:', e);
    }
  }

  // DOM Elements Cache
  const elements = {
    themeToggleBtn: document.getElementById('theme-toggle-btn'),
    langBtns: document.querySelectorAll('.lang-btn'),
    navTabs: document.querySelectorAll('.nav-tab'),
    mainContent: document.getElementById('main-content'),
    totalQuestionsCount: document.getElementById('total-q-count'),
    completedQuestionsCount: document.getElementById('completed-q-count'),
    accuracyRate: document.getElementById('accuracy-rate'),
    progressBarFill: document.getElementById('progress-bar-fill'),
    bookmarkCountBadge: document.getElementById('nav-bookmark-count'),
    flashcardCountBadge: document.getElementById('nav-flashcard-count')
  };

  // Init Application
  function init() {
    applyTheme(state.theme);
    setupEventListeners();
    updateNavigationBadges();
    updateGlobalStats();
    renderCurrentTab();
  }

  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
      elements.themeToggleBtn.setAttribute('title', theme === 'dark' ? 'Chuyển sang Giao diện Sáng' : 'Chuyển sang Giao diện Tối');
    }
    saveState();
  }

  function setupEventListeners() {
    // Theme toggle
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', () => {
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      });
    }

    // Global Language switcher
    elements.langBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        elements.langBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.lang = btn.dataset.lang;
        saveState();
        renderCurrentTab();
      });
    });

    // Navigation Tabs
    elements.navTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        elements.navTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        state.currentTab = tab.dataset.tab;
        saveState();
        renderCurrentTab();
      });
    });

    // Keyboard shortcuts for Flashcard
    window.addEventListener('keydown', (e) => {
      if (state.currentTab === 'flashcard') {
        if (e.code === 'Space') {
          e.preventDefault();
          toggleFlashcardFlip();
        } else if (e.code === 'ArrowRight') {
          e.preventDefault();
          nextFlashcard();
        } else if (e.code === 'ArrowLeft') {
          e.preventDefault();
          prevFlashcard();
        }
      }
    });
  }

  function updateNavigationBadges() {
    if (elements.bookmarkCountBadge) {
      elements.bookmarkCountBadge.textContent = state.bookmarks.length;
    }
    if (elements.flashcardCountBadge) {
      elements.flashcardCountBadge.textContent = `${state.flashcardMastered.length}/${CDAC_QUESTIONS.length}`;
    }
  }

  function updateGlobalStats() {
    const total = CDAC_QUESTIONS.length;
    const answeredCount = Object.keys(state.answers).length;
    let correctCount = 0;

    Object.values(state.answers).forEach(ans => {
      if (ans.isCorrect) correctCount++;
    });

    const percentDone = total > 0 ? Math.round((answeredCount / total) * 100) : 0;
    const accuracy = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;

    if (elements.totalQuestionsCount) elements.totalQuestionsCount.textContent = total;
    if (elements.completedQuestionsCount) elements.completedQuestionsCount.textContent = `${answeredCount} / ${total} (${percentDone}%)`;
    if (elements.accuracyRate) elements.accuracyRate.textContent = `${accuracy}% (${correctCount} đúng)`;
    if (elements.progressBarFill) elements.progressBarFill.style.width = `${percentDone}%`;
  }

  function renderCurrentTab() {
    elements.navTabs.forEach(t => {
      if (t.dataset.tab === state.currentTab) t.classList.add('active');
      else t.classList.remove('active');
    });

    elements.langBtns.forEach(b => {
      if (b.dataset.lang === state.lang) b.classList.add('active');
      else b.classList.remove('active');
    });

    switch (state.currentTab) {
      case 'practice':
        renderPracticeMode();
        break;
      case 'flashcard':
        renderFlashcardMode();
        break;
      case 'exam':
        renderExamMode();
        break;
      case 'bookmarks':
        renderBookmarksMode();
        break;
      default:
        renderPracticeMode();
    }

    updateNavigationBadges();
    updateGlobalStats();
  }

  // =========================================================================
  // 1. PRACTICE MODE (Luyện tập từng câu theo Module & Tìm kiếm)
  // =========================================================================
  function renderPracticeMode() {
    const questions = getFilteredQuestions();

    let html = `
      <div class="filter-card">
        <div class="filter-row-top">
          <div class="search-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="practice-search-input" placeholder="Tìm kiếm câu hỏi, từ khóa SQL (ví dụ: NVL, HAVING, 3NF, TRUNCATE...)" value="${escapeHtml(state.searchQuery)}">
          </div>
          <select id="practice-module-select" class="module-select">
            <option value="0" ${state.selectedModule === 0 ? 'selected' : ''}>📚 Tất cả 13 Modules (260 câu)</option>
            ${CDAC_MODULES.map(m => `
              <option value="${m.id}" ${state.selectedModule === m.id ? 'selected' : ''}>
                ${m.title_vi} (${m.question_count} câu)
              </option>
            `).join('')}
          </select>
        </div>

        <div class="status-filter-pills">
          <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-right: 4px;">Trạng thái:</span>
          <button class="pill-btn ${state.statusFilter === 'all' ? 'active' : ''}" data-filter="all">Tất cả (${CDAC_QUESTIONS.length})</button>
          <button class="pill-btn ${state.statusFilter === 'unanswered' ? 'active' : ''}" data-filter="unanswered">Chưa làm</button>
          <button class="pill-btn ${state.statusFilter === 'correct' ? 'active' : ''}" data-filter="correct">Đã làm đúng</button>
          <button class="pill-btn ${state.statusFilter === 'wrong' ? 'active' : ''}" data-filter="wrong">Làm sai</button>
          <button class="pill-btn ${state.statusFilter === 'bookmarked' ? 'active' : ''}" data-filter="bookmarked">⭐ Đã lưu (${state.bookmarks.length})</button>
          
          <button id="btn-reset-filter" class="btn-fc-nav" style="margin-left: auto; padding: 4px 10px; font-size: 0.78rem;">Đặt lại bộ lọc</button>
        </div>
      </div>

      <div class="questions-count-bar" style="margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
        <span style="font-size: 0.92rem; font-weight: 600; color: var(--text-muted);">
          Hiển thị <strong>${questions.length}</strong> / ${CDAC_QUESTIONS.length} câu hỏi
        </span>
        <button id="btn-clear-all-answers" class="btn-fc-nav" style="padding: 4px 10px; font-size: 0.78rem; color: var(--danger);">
          🗑️ Xóa lịch sử trả lời
        </button>
      </div>

      <div class="questions-list-container">
        ${questions.length === 0 ? `
          <div style="text-align: center; padding: 60px 20px; background: var(--bg-secondary); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
            <div style="font-size: 3rem; margin-bottom: 12px;">🔎</div>
            <h3 style="margin-bottom: 8px;">Không tìm thấy câu hỏi phù hợp</h3>
            <p style="color: var(--text-muted);">Thử thay đổi từ khóa tìm kiếm hoặc chọn lại bộ lọc trạng thái.</p>
          </div>
        ` : questions.map(q => renderQuestionCard(q)).join('')}
      </div>
    `;

    elements.mainContent.innerHTML = html;

    // Attach Event Listeners for Filter Card
    const searchInput = document.getElementById('practice-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        saveState();
        renderPracticeQuestionsOnly();
      });
    }

    const moduleSelect = document.getElementById('practice-module-select');
    if (moduleSelect) {
      moduleSelect.addEventListener('change', (e) => {
        state.selectedModule = parseInt(e.target.value, 10);
        saveState();
        renderPracticeQuestionsOnly();
      });
    }

    const filterPills = document.querySelectorAll('.status-filter-pills .pill-btn');
    filterPills.forEach(pill => {
      pill.addEventListener('click', () => {
        filterPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.statusFilter = pill.dataset.filter;
        saveState();
        renderPracticeQuestionsOnly();
      });
    });

    const resetFilterBtn = document.getElementById('btn-reset-filter');
    if (resetFilterBtn) {
      resetFilterBtn.addEventListener('click', () => {
        state.searchQuery = '';
        state.selectedModule = 0;
        state.statusFilter = 'all';
        saveState();
        renderPracticeMode();
      });
    }

    const clearAnswersBtn = document.getElementById('btn-clear-all-answers');
    if (clearAnswersBtn) {
      clearAnswersBtn.addEventListener('click', () => {
        if (confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử trả lời câu hỏi để làm lại từ đầu không?')) {
          state.answers = {};
          saveState();
          updateGlobalStats();
          renderPracticeMode();
        }
      });
    }

    attachQuestionCardListeners();
  }

  function renderPracticeQuestionsOnly() {
    const questions = getFilteredQuestions();
    const container = document.querySelector('.questions-list-container');
    const countBar = document.querySelector('.questions-count-bar span');
    if (countBar) {
      countBar.innerHTML = `Hiển thị <strong>${questions.length}</strong> / ${CDAC_QUESTIONS.length} câu hỏi`;
    }
    if (container) {
      if (questions.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 60px 20px; background: var(--bg-secondary); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
            <div style="font-size: 3rem; margin-bottom: 12px;">🔎</div>
            <h3 style="margin-bottom: 8px;">Không tìm thấy câu hỏi phù hợp</h3>
            <p style="color: var(--text-muted);">Thử thay đổi từ khóa tìm kiếm hoặc chọn lại bộ lọc trạng thái.</p>
          </div>
        `;
      } else {
        container.innerHTML = questions.map(q => renderQuestionCard(q)).join('');
        attachQuestionCardListeners();
      }
    }
  }

  function getFilteredQuestions() {
    return CDAC_QUESTIONS.filter(q => {
      // 1. Module filter
      if (state.selectedModule !== 0 && q.module_id !== state.selectedModule) {
        return false;
      }

      // 2. Status filter
      const ans = state.answers[q.id];
      const isBookmarked = state.bookmarks.includes(q.id);

      if (state.statusFilter === 'unanswered' && ans) return false;
      if (state.statusFilter === 'correct' && (!ans || !ans.isCorrect)) return false;
      if (state.statusFilter === 'wrong' && (!ans || ans.isCorrect)) return false;
      if (state.statusFilter === 'bookmarked' && !isBookmarked) return false;

      // 3. Search query
      if (state.searchQuery.trim()) {
        const query = state.searchQuery.toLowerCase();
        const inPrompt = q.prompt_en.toLowerCase().includes(query) || q.prompt_vi.toLowerCase().includes(query);
        const inExpl = q.explanation_vi.toLowerCase().includes(query);
        const inOpts = q.options.some(o => o.text_en.toLowerCase().includes(query) || o.text_vi.toLowerCase().includes(query));
        if (!inPrompt && !inExpl && !inOpts) return false;
      }

      return true;
    });
  }

  function renderQuestionCard(q, isExamMode = false, examUserSelection = null) {
    const isBookmarked = state.bookmarks.includes(q.id);
    const ansRecord = state.answers[q.id];
    const userSelected = isExamMode ? examUserSelection : (ansRecord ? ansRecord.selected : null);
    const hasAnswered = userSelected !== null && userSelected !== undefined;

    // Check individual translation preference override
    const langMode = q._langOverride || state.lang; // 'vi', 'bilingual', 'en'

    const promptFormatted = formatPromptWithCode(langMode === 'vi' ? q.prompt_vi : q.prompt_en);
    const subViFormatted = (langMode === 'bilingual') ? `<div class="q-prompt-sub-vi">🇻🇳 <em>${escapeHtml(q.prompt_vi)}</em></div>` : '';

    return `
      <div class="question-card" id="q-card-${q.id}" data-qid="${q.id}">
        <div class="q-header">
          <div class="q-meta">
            <span class="q-badge-num">Câu ${q.id}</span>
            <span class="q-badge-mod">${q.module_name_vi}</span>
          </div>
          <div class="q-actions">
            ${!isExamMode ? `
              <button class="btn-translate-q" data-qid="${q.id}" title="Chuyển đổi ngôn ngữ câu hỏi">
                🌐 ${langMode === 'vi' ? 'Tiếng Việt' : (langMode === 'en' ? 'English' : 'Song ngữ')}
              </button>
              <button class="btn-icon btn-bookmark ${isBookmarked ? 'bookmarked' : ''}" data-qid="${q.id}" title="${isBookmarked ? 'Bỏ lưu câu hỏi này' : 'Lưu câu hỏi khó này'}">
                ${isBookmarked ? '⭐' : '☆'}
              </button>
            ` : ''}
          </div>
        </div>

        <div class="q-body">
          <div class="q-prompt-text">${promptFormatted}</div>
          ${subViFormatted}
        </div>

        <div class="q-options">
          ${q.options.map(opt => {
            let itemClass = 'option-item';
            if (isExamMode) {
              if (userSelected === opt.key) itemClass += ' selected';
            } else {
              if (hasAnswered) {
                itemClass += ' locked';
                if (opt.key === q.answer) {
                  itemClass += ' correct';
                } else if (userSelected === opt.key && !opt.is_correct) {
                  itemClass += ' wrong';
                }
              }
            }

            const optTextEn = escapeHtml(opt.text_en);
            const optTextVi = escapeHtml(opt.text_vi);

            return `
              <div class="${itemClass}" data-qid="${q.id}" data-key="${opt.key}">
                <div class="option-key">${opt.key}</div>
                <div class="option-text-wrapper">
                  ${langMode === 'vi' ? `
                    <div class="option-text-en">${optTextVi}</div>
                  ` : (langMode === 'en' ? `
                    <div class="option-text-en">${optTextEn}</div>
                  ` : `
                    <div class="option-text-en">${optTextEn}</div>
                    <div class="option-text-vi">🇻🇳 ${optTextVi}</div>
                  `)}
                </div>
              </div>
            `;
          }).join('')}
        </div>

        ${(!isExamMode && hasAnswered) ? `
          <div class="lecturer-explanation">
            <div class="explanation-header">
              <span>🎓 Lời giảng & Phân tích chuyên sâu của Giảng viên:</span>
              <div style="margin-left: auto; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 0.85rem; color: var(--success); font-weight: 700;">
                  Đáp án chuẩn: <strong>${q.answer}</strong>
                </span>
                <button class="btn-retry-q" data-qid="${q.id}" style="background: var(--bg-secondary); border: 1px solid var(--border-color); padding: 3px 8px; border-radius: 6px; font-size: 0.75rem; cursor: pointer; color: var(--primary); font-weight: 600;">
                  🔄 Làm lại
                </button>
              </div>
            </div>
            <div class="explanation-body">
              ${q.explanation_vi.replace(/\n/g, '<br>')}
            </div>
            ${q.key_takeaway_vi ? `
              <div class="key-takeaway-box">
                💡 <strong>Ghi nhớ cốt lõi:</strong> ${escapeHtml(q.key_takeaway_vi)}
              </div>
            ` : ''}
          </div>
        ` : ''}
      </div>
    `;
  }

  function formatPromptWithCode(text) {
    if (!text) return '';

    const lines = text.split('\n');
    let inSql = false;
    let sqlBuffer = [];
    let result = [];

    for (let line of lines) {
      const trimmed = line.trim();
      const isSqlKeyword = /^(SELECT|FROM|WHERE|INSERT|UPDATE|DELETE|MERGE|CREATE|ALTER|DROP|TRUNCATE|GROUP BY|HAVING|ORDER BY|ON|WHEN|VALUES)\b/i.test(trimmed);
      const isTableSchema = /^(Column Name|Table Name|PRODUCT_ID|EMPLOYEE_ID|STD_ID|CLASS_ID|EVENT_ID|Customer|Tournament)\b/i.test(trimmed);

      if (isSqlKeyword || isTableSchema || inSql) {
        const isQuestionEnd = /\?$/.test(trimmed) || /^(Which|What|How|Evaluate|You need|Why)\b/i.test(trimmed);
        if (isQuestionEnd && sqlBuffer.length > 0) {
          result.push(`<pre class="sql-code"><code>${escapeHtml(sqlBuffer.join('\n'))}</code></pre>`);
          sqlBuffer = [];
          inSql = false;
          result.push(escapeHtml(line));
        } else {
          inSql = true;
          sqlBuffer.push(line);
        }
      } else {
        result.push(escapeHtml(line));
      }
    }

    if (sqlBuffer.length > 0) {
      result.push(`<pre class="sql-code"><code>${escapeHtml(sqlBuffer.join('\n'))}</code></pre>`);
    }

    return result.join('<br>');
  }

  function attachQuestionCardListeners() {
    // 1. Option click for Practice Mode
    document.querySelectorAll('.question-card:not(.exam-card) .option-item:not(.locked)').forEach(item => {
      item.addEventListener('click', function () {
        const qid = parseInt(this.dataset.qid, 10);
        const key = this.dataset.key;
        selectOptionInPractice(qid, key);
      });
    });

    // 2. Individual translation button
    document.querySelectorAll('.btn-translate-q').forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const qid = parseInt(this.dataset.qid, 10);
        toggleQuestionLanguage(qid);
      });
    });

    // 3. Bookmark button
    document.querySelectorAll('.btn-bookmark').forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const qid = parseInt(this.dataset.qid, 10);
        toggleBookmark(qid);
      });
    });

    // 4. Retry question button
    document.querySelectorAll('.btn-retry-q').forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const qid = parseInt(this.dataset.qid, 10);
        retryQuestion(qid);
      });
    });
  }

  function retryQuestion(qid) {
    delete state.answers[qid];
    saveState();
    updateGlobalStats();

    const q = CDAC_QUESTIONS.find(item => item.id === qid);
    if (!q) return;

    const cardEl = document.getElementById(`q-card-${qid}`);
    if (cardEl) {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = renderQuestionCard(q);
      const newCard = tempDiv.firstElementChild;
      cardEl.replaceWith(newCard);
      attachCardListenersForSingle(newCard);
    }
  }

  function selectOptionInPractice(qid, selectedKey) {
    const q = CDAC_QUESTIONS.find(item => item.id === qid);
    if (!q) return;

    const isCorrect = (selectedKey === q.answer);
    state.answers[qid] = {
      selected: selectedKey,
      isCorrect: isCorrect,
      answeredAt: Date.now()
    };
    saveState();
    updateGlobalStats();

    const cardEl = document.getElementById(`q-card-${qid}`);
    if (cardEl) {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = renderQuestionCard(q);
      const newCard = tempDiv.firstElementChild;
      cardEl.replaceWith(newCard);
      attachCardListenersForSingle(newCard);
    }
  }

  function toggleQuestionLanguage(qid) {
    const q = CDAC_QUESTIONS.find(item => item.id === qid);
    if (!q) return;

    const current = q._langOverride || state.lang;
    const cycle = { 'bilingual': 'vi', 'vi': 'en', 'en': 'bilingual' };
    q._langOverride = cycle[current] || 'vi';

    const cardEl = document.getElementById(`q-card-${qid}`);
    if (cardEl) {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = renderQuestionCard(q);
      const newCard = tempDiv.firstElementChild;
      cardEl.replaceWith(newCard);
      attachCardListenersForSingle(newCard);
    }
  }

  function toggleBookmark(qid) {
    const idx = state.bookmarks.indexOf(qid);
    if (idx >= 0) {
      state.bookmarks.splice(idx, 1);
    } else {
      state.bookmarks.push(qid);
    }
    saveState();
    updateNavigationBadges();

    const cardEl = document.getElementById(`q-card-${qid}`);
    if (cardEl) {
      const btn = cardEl.querySelector('.btn-bookmark');
      if (btn) {
        const isBookmarked = state.bookmarks.includes(qid);
        btn.classList.toggle('bookmarked', isBookmarked);
        btn.innerHTML = isBookmarked ? '⭐' : '☆';
      }
    }
  }

  function attachCardListenersForSingle(card) {
    card.querySelectorAll('.option-item:not(.locked)').forEach(item => {
      item.addEventListener('click', function () {
        const qid = parseInt(this.dataset.qid, 10);
        const key = this.dataset.key;
        selectOptionInPractice(qid, key);
      });
    });

    const transBtn = card.querySelector('.btn-translate-q');
    if (transBtn) {
      transBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleQuestionLanguage(parseInt(this.dataset.qid, 10));
      });
    }

    const bookmarkBtn = card.querySelector('.btn-bookmark');
    if (bookmarkBtn) {
      bookmarkBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleBookmark(parseInt(this.dataset.qid, 10));
      });
    }

    const retryBtn = card.querySelector('.btn-retry-q');
    if (retryBtn) {
      retryBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        retryQuestion(parseInt(this.dataset.qid, 10));
      });
    }
  }

  // =========================================================================
  // 2. FLASHCARD MODE (Thẻ ghi nhớ lật mặt 3D & Spaced Repetition)
  // =========================================================================
  let flashcardDeck = [];

  function renderFlashcardMode() {
    flashcardDeck = CDAC_QUESTIONS.filter(q => {
      if (state.selectedModule !== 0 && q.module_id !== state.selectedModule) return false;
      return true;
    });

    if (state.flashcardIndex >= flashcardDeck.length) {
      state.flashcardIndex = 0;
    }

    const q = flashcardDeck[state.flashcardIndex];
    const isMastered = q ? state.flashcardMastered.includes(q.id) : false;
    const isBookmarked = q ? state.bookmarks.includes(q.id) : false;

    let html = `
      <div class="flashcard-section">
        <div class="flashcard-controls-top">
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <select id="fc-module-select" class="module-select" style="min-width: 250px;">
              <option value="0" ${state.selectedModule === 0 ? 'selected' : ''}>📚 Tất cả Modules (${CDAC_QUESTIONS.length} thẻ)</option>
              ${CDAC_MODULES.map(m => `
                <option value="${m.id}" ${state.selectedModule === m.id ? 'selected' : ''}>
                  ${m.title_vi} (${m.question_count} thẻ)
                </option>
              `).join('')}
            </select>
            <button id="btn-fc-shuffle" class="btn-fc-nav" title="Xáo trộn ngẫu nhiên thứ tự thẻ">
              🎲 Trộn thẻ
            </button>
          </div>

          <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 0.95rem; font-weight: 700; color: var(--primary);">
              Thẻ ${state.flashcardIndex + 1} / ${flashcardDeck.length}
            </span>
            <span style="background: var(--success-bg); color: var(--success); padding: 4px 10px; border-radius: 999px; font-size: 0.8rem; font-weight: 600;">
              ✓ Đã thuộc: ${state.flashcardMastered.length}
            </span>
          </div>
        </div>

        ${!q ? `
          <div style="padding: 60px; text-align: center; background: var(--bg-secondary); border-radius: var(--radius-xl); width: 100%;">
            <h3>Không có thẻ nào trong bộ lọc này</h3>
          </div>
        ` : `
          <div class="flashcard-scene" id="flashcard-scene">
            <div class="flashcard-card ${state.flashcardIsFlipped ? 'is-flipped' : ''}" id="flashcard-card">
              <!-- FRONT OF CARD -->
              <div class="flashcard-face flashcard-face-front">
                <div class="card-top-bar">
                  <span class="q-badge-num">Câu ${q.id}</span>
                  <span class="q-badge-mod">${q.module_name_vi}</span>
                  <div style="margin-left: auto; display: flex; gap: 8px;">
                    <button class="btn-icon btn-bookmark ${isBookmarked ? 'bookmarked' : ''}" data-qid="${q.id}" id="fc-bookmark-btn">
                      ${isBookmarked ? '⭐' : '☆'}
                    </button>
                  </div>
                </div>

                <div class="card-content-center">
                  <div style="font-size: 0.82rem; font-weight: 700; color: var(--text-light); text-transform: uppercase; margin-bottom: 6px;">
                    🇬🇧 CÂU HỎI TIẾNG ANH (ORIGINAL):
                  </div>
                  <div style="font-size: 1.15rem; font-weight: 600; line-height: 1.55; margin-bottom: 14px;">
                    ${formatPromptWithCode(q.prompt_en)}
                  </div>

                  <div style="font-size: 0.82rem; font-weight: 700; color: var(--primary); text-transform: uppercase; margin-bottom: 4px;">
                    🇻🇳 BẢN DỊCH TIẾNG VIỆT:
                  </div>
                  <div style="font-size: 1.05rem; color: #0369a1; background: var(--primary-light); padding: 10px 14px; border-radius: var(--radius-sm); border-left: 4px solid var(--primary); line-height: 1.5;">
                    ${escapeHtml(q.prompt_vi)}
                  </div>
                </div>

                <div class="card-flip-prompt">
                  <span>🔄 Nhấp vào thẻ hoặc bấm phím <strong>Space</strong> để lật xem đáp án & lời giải</span>
                </div>
              </div>

              <!-- BACK OF CARD -->
              <div class="flashcard-face flashcard-face-back">
                <div class="card-top-bar">
                  <span style="background: var(--success); color: white; padding: 4px 12px; border-radius: var(--radius-sm); font-weight: 700; font-size: 0.95rem;">
                    ✓ ĐÁP ÁN ĐÚNG: ${q.answer}
                  </span>
                  <span class="q-badge-mod">${q.module_name_vi}</span>
                </div>

                <div class="card-content-center" style="overflow-y: auto; max-height: 300px;">
                  <div style="font-size: 1.05rem; font-weight: 700; color: var(--success); margin-bottom: 12px; padding: 8px 12px; background: var(--success-bg); border-radius: var(--radius-sm); border: 1px solid var(--success-border);">
                    ${escapeHtml(q.options.find(o => o.key === q.answer)?.text_vi || '')}
                  </div>

                  <div style="font-size: 0.92rem; line-height: 1.6; color: var(--text-main); margin-bottom: 12px;">
                    <strong>🎓 Lời giảng của Giảng viên:</strong><br>
                    ${q.explanation_vi.replace(/\n/g, '<br>')}
                  </div>

                  ${q.key_takeaway_vi ? `
                    <div class="key-takeaway-box" style="margin-top: 8px;">
                      💡 <strong>Ghi nhớ cốt lõi:</strong> ${escapeHtml(q.key_takeaway_vi)}
                    </div>
                  ` : ''}
                </div>

                <div class="card-flip-prompt">
                  <span>🔄 Nhấp vào thẻ để quay lại câu hỏi</span>
                </div>
              </div>
            </div>
          </div>

          <div class="flashcard-actions-bottom">
            <button id="fc-prev-btn" class="btn-fc-nav" ${state.flashcardIndex === 0 ? 'disabled' : ''}>
              ← Thẻ trước
            </button>

            <button id="fc-toggle-master-btn" class="btn-fc-nav ${isMastered ? 'btn-fc-review' : 'btn-fc-master'}">
              ${isMastered ? '🔄 Cần ôn thêm' : '✅ Đã thuộc thẻ này'}
            </button>

            <button id="fc-flip-btn" class="btn-fc-nav">
              🔄 Lật thẻ (Space)
            </button>

            <button id="fc-next-btn" class="btn-fc-nav" ${state.flashcardIndex === flashcardDeck.length - 1 ? 'disabled' : ''}>
              Thẻ tiếp theo →
            </button>
          </div>
        `}
      </div>
    `;

    elements.mainContent.innerHTML = html;

    // Attach Event Listeners
    const cardEl = document.getElementById('flashcard-card');
    if (cardEl) {
      cardEl.addEventListener('click', toggleFlashcardFlip);
    }

    const flipBtn = document.getElementById('fc-flip-btn');
    if (flipBtn) {
      flipBtn.addEventListener('click', toggleFlashcardFlip);
    }

    const nextBtn = document.getElementById('fc-next-btn');
    if (nextBtn) {
      nextBtn.addEventListener('click', nextFlashcard);
    }

    const prevBtn = document.getElementById('fc-prev-btn');
    if (prevBtn) {
      prevBtn.addEventListener('click', prevFlashcard);
    }

    const masterBtn = document.getElementById('fc-toggle-master-btn');
    if (masterBtn && q) {
      masterBtn.addEventListener('click', () => {
        toggleMasterFlashcard(q.id);
      });
    }

    const shuffleBtn = document.getElementById('btn-fc-shuffle');
    if (shuffleBtn) {
      shuffleBtn.addEventListener('click', () => {
        for (let i = flashcardDeck.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [flashcardDeck[i], flashcardDeck[j]] = [flashcardDeck[j], flashcardDeck[i]];
        }
        state.flashcardIndex = 0;
        state.flashcardIsFlipped = false;
        renderFlashcardMode();
      });
    }

    const modSelect = document.getElementById('fc-module-select');
    if (modSelect) {
      modSelect.addEventListener('change', (e) => {
        state.selectedModule = parseInt(e.target.value, 10);
        state.flashcardIndex = 0;
        state.flashcardIsFlipped = false;
        saveState();
        renderFlashcardMode();
      });
    }

    const bmBtn = document.getElementById('fc-bookmark-btn');
    if (bmBtn && q) {
      bmBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleBookmark(q.id);
        renderFlashcardMode();
      });
    }
  }

  function toggleFlashcardFlip() {
    state.flashcardIsFlipped = !state.flashcardIsFlipped;
    const cardEl = document.getElementById('flashcard-card');
    if (cardEl) {
      cardEl.classList.toggle('is-flipped', state.flashcardIsFlipped);
    }
  }

  function nextFlashcard() {
    if (state.flashcardIndex < flashcardDeck.length - 1) {
      state.flashcardIndex++;
      state.flashcardIsFlipped = false;
      renderFlashcardMode();
    }
  }

  function prevFlashcard() {
    if (state.flashcardIndex > 0) {
      state.flashcardIndex--;
      state.flashcardIsFlipped = false;
      renderFlashcardMode();
    }
  }

  function toggleMasterFlashcard(qid) {
    const idx = state.flashcardMastered.indexOf(qid);
    if (idx >= 0) {
      state.flashcardMastered.splice(idx, 1);
    } else {
      state.flashcardMastered.push(qid);
    }
    saveState();
    updateNavigationBadges();
    renderFlashcardMode();
  }

  // =========================================================================
  // 3. MOCK EXAM MODE (Thi thử đếm ngược thời gian & Đánh giá)
  // =========================================================================
  function renderExamMode() {
    if (!state.exam.inProgress && !state.exam.submitted) {
      renderExamSetup();
    } else if (state.exam.inProgress) {
      renderExamInProgress();
    } else if (state.exam.submitted) {
      renderExamResults();
    }
  }

  function renderExamSetup() {
    let html = `
      <div class="exam-section">
        <div class="exam-setup-card">
          <div style="font-size: 3rem; margin-bottom: 12px;">⏱️</div>
          <h2 class="exam-setup-title">Phòng Thi Thử Mô Phỏng Trắc Nghiệm CDAC DBMS</h2>
          <p class="exam-setup-desc">
            Kiểm tra trình độ kiến thức cơ sở dữ liệu với áp lực thời gian thực tế. Đề thi được chọn ngẫu nhiên từ 260 câu hỏi chuẩn CDAC với giải thích chi tiết sau khi nộp bài.
          </p>

          <div class="exam-options-grid">
            <div class="exam-config-item">
              <label class="exam-config-label">Phạm vi câu hỏi:</label>
              <select id="exam-scope-select">
                <option value="all">Tổng hợp ngẫu nhiên cả 13 Modules</option>
                ${CDAC_MODULES.map(m => `
                  <option value="${m.id}">${m.title_vi}</option>
                `).join('')}
              </select>
            </div>

            <div class="exam-config-item">
              <label class="exam-config-label">Số lượng câu thi:</label>
              <select id="exam-count-select">
                <option value="20">20 câu (Khuyên dùng - Chuẩn module)</option>
                <option value="40">40 câu (Đề thi giữa kỳ)</option>
                <option value="60">60 câu (Đề thi thử nâng cao)</option>
              </select>
            </div>

            <div class="exam-config-item">
              <label class="exam-config-label">Thời gian làm bài:</label>
              <select id="exam-time-select">
                <option value="20">20 phút (1 phút / câu)</option>
                <option value="30">30 phút (Thư thả)</option>
                <option value="15">15 phút (Thử thách tốc độ)</option>
              </select>
            </div>
          </div>

          <button id="btn-start-exam" class="btn-primary" style="font-size: 1.1rem; padding: 14px 40px;">
            🚀 Bắt Đầu Làm Bài Thi
          </button>
        </div>
      </div>
    `;

    elements.mainContent.innerHTML = html;

    const startBtn = document.getElementById('btn-start-exam');
    if (startBtn) {
      startBtn.addEventListener('click', startExam);
    }
  }

  function startExam() {
    const scope = document.getElementById('exam-scope-select').value;
    const count = parseInt(document.getElementById('exam-count-select').value, 10);
    const minutes = parseInt(document.getElementById('exam-time-select').value, 10);

    let candidates = CDAC_QUESTIONS;
    if (scope !== 'all') {
      const mId = parseInt(scope, 10);
      candidates = CDAC_QUESTIONS.filter(q => q.module_id === mId);
    }

    const shuffled = [...candidates].sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, Math.min(count, shuffled.length));

    state.exam = {
      inProgress: true,
      questions: selected,
      userAnswers: {},
      timeRemaining: minutes * 60,
      totalTime: minutes * 60,
      submitted: false,
      score: 0
    };
    saveState();

    startExamTimer();
    renderExamInProgress();
  }

  function startExamTimer() {
    if (timerInterval) clearInterval(timerInterval);

    timerInterval = setInterval(() => {
      if (state.exam.timeRemaining > 0) {
        state.exam.timeRemaining--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        alert('⏰ Đã hết thời gian làm bài! Hệ thống sẽ tự động nộp bài thi của bạn.');
        submitExam();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const timerEl = document.getElementById('exam-timer-val');
    if (timerEl) {
      const m = Math.floor(state.exam.timeRemaining / 60);
      const s = state.exam.timeRemaining % 60;
      timerEl.textContent = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
      if (state.exam.timeRemaining < 180) {
        timerEl.style.color = '#ef4444';
      }
    }
  }

  function renderExamInProgress() {
    const exam = state.exam;
    const answeredCount = Object.keys(exam.userAnswers).length;
    const totalCount = exam.questions.length;

    let html = `
      <div class="exam-section">
        <div class="exam-bar-sticky">
          <div class="exam-timer">
            <span>⏱️</span>
            <span id="exam-timer-val">--:--</span>
          </div>

          <div style="font-size: 0.92rem; font-weight: 600; color: var(--text-muted);">
            Đã làm: <strong style="color: var(--primary);">${answeredCount}</strong> / ${totalCount} câu
          </div>

          <button id="btn-submit-exam" class="btn-primary" style="padding: 8px 20px; font-size: 0.95rem; background: #059669;">
            ✅ Nộp Bài Thi
          </button>
        </div>

        <div style="margin-bottom: 24px; background: var(--bg-secondary); padding: 14px 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
          <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted); margin-bottom: 8px;">
            Bảng theo dõi câu hỏi (Nhấp vào số câu để cuộn đến):
          </div>
          <div class="exam-palette">
            ${exam.questions.map((q, idx) => {
              const isAnswered = exam.userAnswers[q.id] !== undefined;
              return `
                <button class="palette-btn ${isAnswered ? 'answered' : ''}" onclick="document.getElementById('exam-q-${q.id}').scrollIntoView({ behavior: 'smooth', block: 'center' })">
                  ${idx + 1}
                </button>
              `;
            }).join('')}
          </div>
        </div>

        <div class="exam-questions-list">
          ${exam.questions.map((q, idx) => `
            <div id="exam-q-${q.id}" class="exam-question-wrapper" style="margin-bottom: 20px;">
              <div style="font-size: 0.9rem; font-weight: 700; color: var(--primary); margin-bottom: 6px;">
                Câu số ${idx + 1} (Mã gốc: Q${q.id})
              </div>
              ${renderQuestionCard(q, true, exam.userAnswers[q.id])}
            </div>
          `).join('')}
        </div>
      </div>
    `;

    elements.mainContent.innerHTML = html;
    updateTimerDisplay();

    // Attach exam options selection
    document.querySelectorAll('.exam-question-wrapper .option-item').forEach(item => {
      item.addEventListener('click', function () {
        const qid = parseInt(this.dataset.qid, 10);
        const key = this.dataset.key;
        state.exam.userAnswers[qid] = key;
        saveState();

        const card = document.getElementById(`q-card-${qid}`);
        if (card) {
          card.querySelectorAll('.option-item').forEach(o => {
            if (o.dataset.key === key) o.classList.add('selected');
            else o.classList.remove('selected');
          });
        }

        renderExamInProgress();
      });
    });

    const submitBtn = document.getElementById('btn-submit-exam');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        const remaining = totalCount - Object.keys(exam.userAnswers).length;
        let confirmMsg = 'Bạn có chắc chắn muốn nộp bài thi?';
        if (remaining > 0) {
          confirmMsg = `Bạn vẫn còn ${remaining} câu CHƯA TRẢ LỜI. Bạn có chắc chắn muốn nộp bài ngay bây giờ?`;
        }
        if (confirm(confirmMsg)) {
          submitExam();
        }
      });
    }
  }

  function submitExam() {
    if (timerInterval) clearInterval(timerInterval);

    const exam = state.exam;
    exam.inProgress = false;
    exam.submitted = true;

    let correct = 0;
    exam.questions.forEach(q => {
      const uAns = exam.userAnswers[q.id];
      const isRight = (uAns === q.answer);
      if (isRight) correct++;

      if (uAns !== undefined) {
        state.answers[q.id] = {
          selected: uAns,
          isCorrect: isRight,
          answeredAt: Date.now()
        };
      }
    });

    exam.score = Math.round((correct / exam.questions.length) * 100);
    saveState();
    updateGlobalStats();
    renderExamResults();
  }

  function renderExamResults() {
    const exam = state.exam;
    let correctCount = 0;
    exam.questions.forEach(q => {
      if (exam.userAnswers[q.id] === q.answer) correctCount++;
    });

    const total = exam.questions.length;
    const score = exam.score;

    let gradeText = 'Xuất sắc! Bạn nắm rất vững kiến thức CSDL.';
    let gradeColor = '#10b981';
    if (score < 50) {
      gradeText = 'Cần ôn luyện thêm! Hãy xem kỹ lời giải chi tiết bên dưới.';
      gradeColor = '#ef4444';
    } else if (score < 80) {
      gradeText = 'Khá tốt! Cần chú ý thêm một số bẫy trắc nghiệm của CDAC.';
      gradeColor = '#0284c7';
    }

    let html = `
      <div class="exam-section">
        <div class="exam-setup-card" style="margin-bottom: 30px; text-align: center;">
          <div style="font-size: 3.5rem; margin-bottom: 8px;">📊</div>
          <h2 style="font-size: 1.8rem; margin-bottom: 6px;">KẾT QUẢ BÀI THI</h2>
          <div style="font-size: 3.2rem; font-weight: 800; color: ${gradeColor}; margin: 12px 0;">
            ${score} / 100 Điểm
          </div>
          <p style="font-size: 1.1rem; font-weight: 600; color: var(--text-main); margin-bottom: 6px;">
            Số câu trả lời đúng: <strong>${correctCount}</strong> / ${total} câu
          </p>
          <p style="color: var(--text-muted); margin-bottom: 24px;">${gradeText}</p>

          <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
            <button id="btn-retake-exam" class="btn-primary">
              🔄 Làm Bài Thi Khác
            </button>
            <button id="btn-view-practice-exam" class="btn-fc-nav" onclick="window.scrollTo({ top: 500, behavior: 'smooth' })">
              👇 Xem Lại Từng Câu Kèm Lời Giải Chi Tiết
            </button>
          </div>
        </div>

        <h3 style="margin-bottom: 16px; color: var(--text-main);">
          Chi tiết bài thi & Phân tích đáp án:
        </h3>

        <div class="exam-review-list">
          ${exam.questions.map((q, idx) => {
            const uAns = exam.userAnswers[q.id];
            const isRight = (uAns === q.answer);
            return `
              <div style="margin-bottom: 20px; border-left: 5px solid ${isRight ? 'var(--success)' : 'var(--danger)'}; border-radius: var(--radius-md); padding-left: 8px;">
                <div style="font-weight: 700; margin-bottom: 6px; color: ${isRight ? 'var(--success)' : 'var(--danger)'};">
                  Câu ${idx + 1}: ${isRight ? '✓ ĐÚNG (+1 điểm)' : `✗ SAI (Bạn chọn: ${uAns || 'Chưa trả lời'})`}
                </div>
                ${renderQuestionCard(q, false)}
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;

    elements.mainContent.innerHTML = html;

    const retakeBtn = document.getElementById('btn-retake-exam');
    if (retakeBtn) {
      retakeBtn.addEventListener('click', () => {
        state.exam = {
          inProgress: false,
          questions: [],
          userAnswers: {},
          timeRemaining: 0,
          totalTime: 0,
          submitted: false,
          score: 0
        };
        saveState();
        renderExamMode();
      });
    }

    attachQuestionCardListeners();
  }

  // =========================================================================
  // 4. BOOKMARKS MODE (Xem các câu hỏi đã lưu đánh dấu sao)
  // =========================================================================
  function renderBookmarksMode() {
    const bookmarkedQs = CDAC_QUESTIONS.filter(q => state.bookmarks.includes(q.id));

    let html = `
      <div style="margin-bottom: 24px; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 20px 24px; box-shadow: var(--card-shadow); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
        <div>
          <h2 style="font-size: 1.35rem; font-weight: 700; margin-bottom: 4px;">⭐ Danh Sách Câu Hỏi Đã Lưu (${bookmarkedQs.length} câu)</h2>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            Các câu hỏi khó, câu có bẫy hoặc cần ôn lại trước ngày thi.
          </p>
        </div>
        ${bookmarkedQs.length > 0 ? `
          <button id="btn-clear-bookmarks" class="btn-fc-nav" style="color: var(--danger);">
            Xóa tất cả dấu sao
          </button>
        ` : ''}
      </div>

      <div class="bookmarks-list">
        ${bookmarkedQs.length === 0 ? `
          <div style="text-align: center; padding: 70px 20px; background: var(--bg-secondary); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
            <div style="font-size: 3.5rem; margin-bottom: 12px;">⭐</div>
            <h3 style="margin-bottom: 8px;">Bạn chưa lưu câu hỏi nào</h3>
            <p style="color: var(--text-muted); max-width: 480px; margin: 0 auto 16px;">
              Khi đang làm bài ở mục Luyện tập hoặc Thẻ ghi nhớ, bạn có thể bấm vào biểu tượng ngôi sao để lưu lại các câu hỏi khó để xem lại tại đây.
            </p>
            <button class="btn-primary" onclick="document.querySelector('.nav-tab[data-tab=\"practice\"]').click()">
              Đến Mục Luyện Tập Ngay
            </button>
          </div>
        ` : bookmarkedQs.map(q => renderQuestionCard(q)).join('')}
      </div>
    `;

    elements.mainContent.innerHTML = html;

    const clearBtn = document.getElementById('btn-clear-bookmarks');
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        if (confirm('Bạn có chắc muốn xóa tất cả câu hỏi khỏi danh sách đã lưu?')) {
          state.bookmarks = [];
          saveState();
          updateNavigationBadges();
          renderBookmarksMode();
        }
      });
    }

    attachQuestionCardListeners();
  }

  function escapeHtml(text) {
    if (!text) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Run App
  document.addEventListener('DOMContentLoaded', init);

})();
