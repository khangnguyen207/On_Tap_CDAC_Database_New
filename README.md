# 🗄️ CDAC DBMS Master - Hệ Thống Ôn Tập & Khảo Sát Cơ Sở Dữ Liệu Chuyên Sâu

Hệ thống ôn tập toàn diện **260 câu hỏi trắc nghiệm Cơ sở Dữ liệu chuẩn CDAC ACTS**, được số hóa và nâng cấp với góc nhìn của **Lập trình viên kiêm Giảng viên Database**.

---

## 🌟 Điểm nổi bật của hệ thống

1. **Không cần tài khoản (Zero Login / 100% Offline)**:
   - Toàn bộ ứng dụng chạy trực tiếp trên trình duyệt, không cần cài đặt database hay backend.
   - Tiến độ ôn tập, điểm số, danh sách câu hỏi đã lưu (Bookmarks), thẻ Flashcard đã thuộc được lưu tự động trên trình duyệt (`LocalStorage`).

2. **Giao diện xanh pastel dịu mắt (Soft Light Blue Theme)**:
   - Tông màu chủ đạo xanh nhạt pastel (`#0284c7`, `#38bdf8`, `#e0f2fe`) mang lại cảm giác dễ chịu, chống mỏi mắt khi học lâu.
   - Hỗ trợ chế độ **Giao diện tối (Dark Navy Blue)** cho buổi tối.
   - Mã lệnh SQL được định dạng bằng font lập trình (`JetBrains Mono / Fira Code`), dễ đọc và nổi bật.

3. **Nút phiên dịch nhanh & Chế độ Song ngữ (Instant Translation)**:
   - Nút **`🌐 Dịch Tiếng Việt / English`** riêng trên từng câu hỏi để tra cứu nhanh.
   - Thanh công cụ chuyển đổi chế độ xem toàn hệ thống:
     - 🇻🇳 **Chỉ Tiếng Việt**: Dịch chuẩn thuật ngữ chuyên ngành CSDL.
     - 🔄 **Song ngữ (Bilingual)**: Hiển thị câu hỏi tiếng Anh gốc và bản dịch tiếng Việt ngay bên dưới (phương pháp học hiệu quả nhất cho chứng chỉ quốc tế).
     - 🇬🇧 **English**: Hiển thị 100% tiếng Anh gốc.

4. **Nâng cấp lời giảng & Phân tích chuyên sâu của Giảng viên**:
   - File đề ôn gốc của CDAC hoàn toàn không có lời giải (chỉ ghi `"Your answer is correct / incorrect"`).
   - Hệ thống đã bổ sung **phân tích sư phạm chuyên sâu** cho **toàn bộ 260 câu hỏi**:
     - 🎓 **Bản chất kiến thức**: Cơ chế hoạt động của Oracle Instance, SGA, PGA, Background Processes (LGWR, DBWn...), các quy tắc chuẩn hóa (1NF, 2NF, 3NF, BCNF).
     - 🔍 **Vì sao chọn đáp án này**: Phân tích cú pháp và lý do đúng.
     - ⚠️ **Lưu ý bẫy đề thi & Đính chính lỗi đề gốc**: Chỉ ra các lỗi chính tả và sự khác biệt giữa đáp án đề thi và thực tế (ví dụ: Q3 về multiplexing, Q17 lỗi `unsigned charRDBMS`, Q41 TRUNCATE vs DROP, Q72 `VARCNAR2`, Q95 lỗi `PDATE`...).
     - 💡 **Ghi nhớ cốt lõi (Key Takeaways)**: Tóm tắt 1 câu ngắn gọn giúp nhớ nhanh khi vào phòng thi.

5. **Thẻ ghi nhớ Flashcard 3D (Spaced Repetition)**:
   - Lật mặt thẻ 3D mượt mà (bấm chuột hoặc dùng phím **Space**).
   - Mặt trước: Câu hỏi tiếng Anh + dịch tiếng Việt + code SQL.
   - Mặt sau: Đáp án chính xác được highlight + Lời giảng của Giảng viên + Điểm cốt lõi.
   - Nút **`✅ Đã thuộc thẻ này`** / **`🔄 Cần ôn thêm`**.
   - Hỗ trợ xáo trộn ngẫu nhiên thẻ (`🎲 Trộn thẻ`) và lọc theo từng Module.

6. **Chế độ Thi thử đếm giờ (Mock Exam)**:
   - Tùy chọn 20, 40 hoặc 60 câu ngẫu nhiên hoặc theo từng Module.
   - Đồng hồ đếm ngược có cảnh báo thời gian.
   - Bảng ma trận số câu hỏi (Palette) để nhảy nhanh đến câu chưa làm.
   - Nộp bài -> Bảng điểm tổng kết, xếp loại và xem lại toàn bộ câu đúng/sai kèm giải thích.

---

## 📚 Danh mục 13 Modules (260 câu hỏi)

| Module | Tên chuyên đề | Phạm vi câu hỏi |
| :--- | :--- | :--- |
| **Module 1** | Introduction to DBMS (Tổng quan DBMS & Kiến trúc Oracle) | Câu 1 - Câu 20 |
| **Module 2** | Introduction to SQL (Giới thiệu SQL & Mệnh đề SELECT) | Câu 21 - Câu 40 |
| **Module 3** | DDL (Ngôn ngữ định nghĩa dữ liệu: CREATE, ALTER, DROP, TRUNCATE) | Câu 41 - Câu 60 |
| **Module 4** | Constraints (Ràng buộc: PK, FK, UNIQUE, NOT NULL, CHECK) | Câu 61 - Câu 80 |
| **Module 5** | DML (Ngôn ngữ thao tác dữ liệu: INSERT, UPDATE, DELETE, MERGE) | Câu 81 - Câu 100 |
| **Module 6** | Single Row Functions (Hàm chuỗi, số, ngày tháng, NVL, DECODE) | Câu 101 - Câu 120 |
| **Module 7** | Group Functions (Hàm nhóm, GROUP BY, HAVING, WHERE vs HAVING) | Câu 121 - Câu 140 |
| **Module 8** | SQL Joins (Phép kết nối bảng: Equi, Non-equi, Natural, Outer Joins) | Câu 141 - Câu 160 |
| **Module 9** | Sub Queries (Truy vấn con cơ bản, toán tử IN, ANY, ALL, NOT IN với NULL) | Câu 161 - Câu 180 |
| **Module 10**| Advanced Sub Queries (Correlated subquery, EXISTS, WITH CTE, Pairwise) | Câu 181 - Câu 200 |
| **Module 11**| Views (Khung nhìn: Tạo view, FORCE, WITH CHECK OPTION, Inline view) | Câu 201 - Câu 220 |
| **Module 12**| Set Operators & Pseudocolumn (Toán tử tập hợp, ROWNUM, ROWID, LEVEL) | Câu 221 - Câu 240 |
| **Module 13**| Normalization (Chuẩn hóa CSDL: Phụ thuộc hàm, 1NF, 2NF, 3NF, BCNF) | Câu 241 - Câu 260 |

---

## 🚀 Cách mở và sử dụng website

### Cách 1: Chạy trực tiếp (Khuyên dùng)
- Nhấp đúp vào file **`Mo_Trang_Web.bat`** hoặc file **`index.html`**.
- Trang web sẽ mở ngay lập tức trong trình duyệt mặc định của bạn (Chrome, Edge, Firefox, Cốc Cốc...).
- Không cần cài bất cứ phần mềm hay server nào!

### Cách 2: Chạy qua Live Server / Localhost (Nếu thích)
- Có thể dùng VS Code extension *Live Server*, hoặc gõ lệnh terminal:
  ```bash
  python -m http.server 8000
  ```
- Mở địa chỉ `http://localhost:8000` trên trình duyệt.

---

## ⌨️ Phím tắt hỗ trợ trong chế độ Flashcard
- **Phím Space (Dấu cách)**: Lật mặt trước / mặt sau của thẻ ghi nhớ.
- **Phím mũi tên Sang Phải `→`**: Chuyển sang thẻ tiếp theo.
- **Phím mũi tên Sang Trái `←`**: Quay lại thẻ phía trước.
