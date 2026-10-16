# -*- coding: utf-8 -*-
"""
Module 1 (Q1-Q20), Module 2 (Q21-Q40), Module 3 (Q41-Q60)
Comprehensive Bilingual Translations & Lecturer Explanations
"""

DATA_MOD_1_3 = {}

# MODULE 1: Introduction to DBMS (Q1 - Q20)
DATA_MOD_1_3[1] = {
    "prompt_vi": "Đặc điểm nào sau đây KHÔNG PHẢI là một ưu điểm của Hệ quản trị cơ sở dữ liệu (DBMS)?",
    "options_vi": {
        "A": "Tạo dữ liệu ứng dụng của người dùng (User application data creation).",
        "B": "Tính độc lập dữ liệu và truy xuất hiệu quả.",
        "C": "Giảm thiểu thời gian phát triển ứng dụng.",
        "D": "Đảm bảo tính toàn vẹn và an toàn bảo mật dữ liệu."
    },
    "explanation_vi": "Trong kiến trúc hệ thống, DBMS chịu trách nhiệm lưu trữ, bảo vệ, duy trì tính toàn vẹn và cung cấp cơ chế truy xuất dữ liệu độc lập với tầng ứng dụng. Việc 'tạo dữ liệu nghiệp vụ của người dùng' thuộc về phần mềm ứng dụng và người dùng cuối, không phải là ưu điểm do DBMS cung cấp.",
    "key_takeaway_vi": "DBMS quản lý, bảo mật và cung cấp tính độc lập dữ liệu; dữ liệu ứng dụng do người dùng/ứng dụng sinh ra.",
    "flashcard_front_vi": "Vì sao 'User application data creation' KHÔNG PHẢI là ưu điểm của DBMS?",
    "flashcard_back_vi": "Vì việc tạo dữ liệu nghiệp vụ là trách nhiệm của ứng dụng/người dùng; DBMS chỉ đóng vai trò lưu trữ, quản lý và đảm bảo an toàn dữ liệu."
}

DATA_MOD_1_3[2] = {
    "prompt_vi": "Tiến trình nền (Background process) nào trong Oracle sẽ cập nhật các tệp Online Redo Log với các bản ghi từ Redo Log Buffer khi có lệnh COMMIT xảy ra?",
    "options_vi": {
        "A": "LGWR (Log Writer)",
        "B": "DBWn (Database Writer)",
        "C": "CKPT (Checkpoint)",
        "D": "CJQn (Coordinator Job Queue)"
    },
    "explanation_vi": "Tiến trình LGWR (Log Writer) chịu trách nhiệm ghi tuần tự các bản ghi redo từ bộ đệm Redo Log Buffer trên SGA xuống các tệp đĩa Online Redo Log Files. LGWR được kích hoạt ngay khi người dùng COMMIT, hoặc khi bộ đệm đầy 1/3, hoặc định kỳ mỗi 3 giây.",
    "key_takeaway_vi": "Ghi Redo Log khi COMMIT = tiến trình LGWR (Log Writer).",
    "flashcard_front_vi": "Tiến trình nền nào ghi Redo Log Buffer xuống đĩa khi COMMIT?",
    "flashcard_back_vi": "LGWR (Log Writer). DBWn ghi khối dữ liệu dirty block xuống datafile; CKPT đồng bộ thông tin kiểm tra."
}

DATA_MOD_1_3[3] = {
    "prompt_vi": "Những tệp nào sau đây có thể thực hiện cơ chế ghép kênh/nhân bản (multiplexed) trong Oracle?",
    "options_vi": {
        "A": "Data Files (Tệp dữ liệu)",
        "B": "Control Files (Tệp điều khiển)",
        "C": "Parameter Files (Tệp tham số)",
        "D": "Data Buffer Cache (Bộ đệm dữ liệu)"
    },
    "explanation_vi": "⚠️ LƯU Ý ĐỀ THI & THỰC TẾ: Theo chuẩn kiến trúc Oracle, Control Files và Online Redo Log Files hỗ trợ cơ chế Multiplexing trực tiếp bởi Oracle engine để đảm bảo tính sẵn sàng cao. Data Files không hỗ trợ multiplexing nội tại của Oracle. Tuy nhiên, đáp án chính thức trong ngân hàng đề CDAC là A (Data Files) - có thể do lỗi soạn thảo câu hỏi gốc 'Which files CANNOT be multiplexed?'. Sinh viên cần ghi nhớ: Khi thi chọn A theo đáp án CDAC, nhưng phỏng vấn kỹ thuật cần giải thích rõ Control Files và Redo Log Files mới là các tệp được Oracle multiplex!",
    "key_takeaway_vi": "Kiến trúc Oracle chuẩn: Control Files & Redo Log Files được Oracle multiplex. Đáp án đề thi CDAC đánh dấu Data Files.",
    "flashcard_front_vi": "Trong chuẩn Oracle, các tệp nào được cơ chế Multiplexing bảo vệ?",
    "flashcard_back_vi": "Control Files và Redo Log Files. (Lưu ý đáp án ngân hàng đề CDAC chọn A - Data Files)."
}

DATA_MOD_1_3[4] = {
    "prompt_vi": "Phát biểu nào sau đây về Data files (Tệp dữ liệu) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Một Data file chỉ có thể thuộc về duy nhất một Tablespace.",
        "B": "Mỗi Tablespace bắt buộc phải có ít nhất một Data file.",
        "C": "Duy trì nhật ký các thay đổi của cơ sở dữ liệu để phục vụ việc khôi phục (recovery).",
        "D": "Data file chứa dữ liệu cơ sở dữ liệu, bao gồm bảng, chỉ mục, các phân đoạn tạm thời..."
    },
    "explanation_vi": "Phát biểu C sai vì nhiệm vụ duy trì nhật ký các thay đổi để phục hồi dữ liệu là của Redo Log Files và Archive Log Files, không phải của Data Files. Data Files chỉ chứa dữ liệu thực tế của các đối tượng (bảng, chỉ mục, view materialized...).",
    "key_takeaway_vi": "Data files chứa dữ liệu bảng/chỉ mục; Redo log files mới lưu nhật ký phục hồi.",
    "flashcard_front_vi": "Data files có nhiệm vụ lưu nhật ký thay đổi để phục hồi không?",
    "flashcard_back_vi": "KHÔNG. Đó là nhiệm vụ của Redo Log Files (và Archive Log Files)."
}

DATA_MOD_1_3[5] = {
    "prompt_vi": "Phát biểu nào sau đây về tệp tham số khởi tạo Oracle (init.ora) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Bọc trong dấu ngoặc kép bất kỳ giá trị tham số nào có chứa ký tự đặc biệt.",
        "B": "Một tệp tham số khởi tạo chỉ nên chứa các tham số và các chú thích (comments).",
        "C": "Nhiều tham số có thể được chỉ định trên một dòng, ngăn cách bằng dấu cách.",
        "D": "Các tham số phải được chỉ định theo một thứ tự định trước (predefined order)."
    },
    "explanation_vi": "Trong tệp tham số PFILE (init.ora), các dòng tham số có thể đặt theo bất kỳ thứ tự nào. Oracle sẽ đọc toàn bộ tệp khi khởi động Instance và không yêu cầu thứ tự cố định.",
    "key_takeaway_vi": "Tham số trong init.ora không cần tuân theo thứ tự nhất định.",
    "flashcard_front_vi": "Các tham số trong tệp init.ora có bắt buộc theo thứ tự định trước không?",
    "flashcard_back_vi": "Không bắt buộc. Các tham số có thể đặt ở bất kỳ dòng nào."
}

DATA_MOD_1_3[6] = {
    "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về Oracle Instance?",
    "options_vi": {
        "A": "Oracle Instance cung cấp phương thức để truy cập vào cơ sở dữ liệu Oracle.",
        "B": "Oracle Instance là tập hợp dữ liệu được xử lý như một đơn vị, nơi lưu trữ và truy xuất các thông tin liên quan.",
        "C": "Một Oracle Instance chỉ có thể mở và sử dụng một cơ sở dữ liệu tại một thời điểm.",
        "D": "Oracle Instance bao gồm vùng nhớ SGA và các tiến trình nền (background processes)."
    },
    "explanation_vi": "Định nghĩa ở phương án B chính là định nghĩa của Database (Cơ sở dữ liệu vật lý lưu trên đĩa). Oracle Instance là thực thể đang chạy trên bộ nhớ (RAM), bao gồm System Global Area (SGA) và các Background Processes.",
    "key_takeaway_vi": "Oracle Instance = SGA + Background Processes. Database = Tập hợp dữ liệu/tệp vật lý trên đĩa.",
    "flashcard_front_vi": "Oracle Instance gồm những thành phần nào?",
    "flashcard_back_vi": "Instance = Bộ nhớ dùng chung SGA + Các tiến trình nền (Background Processes). Không bao gồm tệp đĩa vật lý."
}

DATA_MOD_1_3[7] = {
    "prompt_vi": "Thành phần nào sau đây KHÔNG THUỘC vùng nhớ System Global Area (SGA)?",
    "options_vi": {
        "A": "Redo Log Buffer",
        "B": "Data Buffer Cache",
        "C": "Parameter Files (Tệp tham số)",
        "D": "Shared Pool"
    },
    "explanation_vi": "SGA (System Global Area) là vùng nhớ dùng chung trên RAM gồm: Database Buffer Cache, Shared Pool, Redo Log Buffer, Large Pool, Java Pool... Parameter Files (init.ora hoặc SPFILE) là các tệp nhị phân hoặc văn bản lưu trên ổ cứng của hệ điều hành, không nằm trong SGA.",
    "key_takeaway_vi": "SGA gồm Buffer Cache, Shared Pool, Redo Log Buffer. Parameter files là tệp trên đĩa.",
    "flashcard_front_vi": "Parameter Files có nằm trong vùng nhớ SGA không?",
    "flashcard_back_vi": "KHÔNG. Parameter Files là tệp cấu hình lưu trên đĩa cứng OS."
}

DATA_MOD_1_3[8] = {
    "prompt_vi": "Phát biểu nào sau đây về Data buffer cache là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Data buffer cache lưu trữ tập hợp các câu lệnh SQL được sử dụng gần đây nhất.",
        "B": "Data buffer cache lưu trữ dữ liệu được truy cập gần đây nhất.",
        "C": "Data buffer cache đọc và ghi dữ liệu đến và từ các tệp dữ liệu (data files).",
        "D": "Kích thước của mỗi bộ đệm trong Data buffer cache bằng kích thước của một Oracle Block."
    },
    "explanation_vi": "Phát biểu A sai vì nơi lưu trữ các câu lệnh SQL đã biên dịch là Library Cache (thuộc Shared Pool). Data Buffer Cache chỉ lưu các khối dữ liệu (data blocks) chứa dữ liệu thực tế đọc từ bảng hoặc chỉ mục.",
    "key_takeaway_vi": "Data Buffer Cache lưu khối dữ liệu bảng/chỉ mục; Library Cache mới lưu câu lệnh SQL.",
    "flashcard_front_vi": "Data Buffer Cache lưu trữ gì trong Oracle SGA?",
    "flashcard_back_vi": "Lưu các khối dữ liệu bảng/chỉ mục gần đây. Câu lệnh SQL được lưu ở Library Cache trong Shared Pool."
}

DATA_MOD_1_3[9] = {
    "prompt_vi": "Phát biểu nào sau đây về Redo log buffer là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Tiến trình máy khách (Client process) trực tiếp ghi nhận các thay đổi vào redo log buffer.",
        "B": "Redo log buffer ghi lại các thay đổi được thực hiện đối với cơ sở dữ liệu.",
        "C": "Tiến trình máy chủ (Server process) ghi nhận các thay đổi vào redo log buffer.",
        "D": "Redo log buffer ghi lại khối bị thay đổi, vị trí thay đổi và giá trị mới."
    },
    "explanation_vi": "Trong kiến trúc Oracle hai tầng/ba tầng, tiến trình Client không có quyền truy cập trực tiếp vào vùng nhớ SGA. Server Process (tiến trình đại diện phía server) mới là tiến trình thực hiện thao tác và ghi các thay đổi vào Redo Log Buffer.",
    "key_takeaway_vi": "Server Process ghi vào Redo Log Buffer; Client Process không bao giờ can thiệp trực tiếp vào SGA.",
    "flashcard_front_vi": "Tiến trình nào ghi các thay đổi vào Redo Log Buffer?",
    "flashcard_back_vi": "Server Process (tiến trình máy chủ). Client process gửi yêu cầu qua giao thức mạng."
}

DATA_MOD_1_3[10] = {
    "prompt_vi": "Thành phần nào sau đây KHÔNG ĐƯỢC lưu trữ trong Library Cache?",
    "options_vi": {
        "A": "Kết quả trả về của các câu lệnh SQL (Results of the SQL statements).",
        "B": "Văn bản gốc của câu lệnh SQL (The text of SQL statement).",
        "C": "Cây cú pháp: phiên bản đã phân tích biên dịch của câu lệnh (Parse Tree).",
        "D": "Kế hoạch thực thi (Execution Plan)."
    },
    "explanation_vi": "Library Cache là một thành phần của Shared Pool, dùng để tối ưu hóa quá trình biên dịch câu lệnh SQL (Soft Parse). Nó lưu: Text của câu lệnh, Cây phân tích (Parse Tree), và Kế hoạch thực thi (Execution Plan). Nó KHÔNG lưu kết quả dữ liệu trả về của câu lệnh.",
    "key_takeaway_vi": "Library Cache lưu: SQL text, Parse Tree, Execution Plan. Không lưu tập kết quả dữ liệu.",
    "flashcard_front_vi": "Library Cache có lưu kết quả thực thi của câu lệnh SQL không?",
    "flashcard_back_vi": "KHÔNG. Library Cache chỉ lưu cú pháp, cây phân tích và kế hoạch thực thi để tái sử dụng."
}

DATA_MOD_1_3[11] = {
    "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về Shared Pool?",
    "options_vi": {
        "A": "Shared Pool có thể được sử dụng bởi nhiều câu lệnh SQL để xử lý dữ liệu được truy xuất.",
        "B": "Shared Pool là một phần của vùng nhớ SGA.",
        "C": "Shared Pool bao gồm Library cache và Data dictionary cache.",
        "D": "Shared Pool được định kích thước bởi tham số SHARED_POOL_SIZE trong init.ora."
    },
    "explanation_vi": "Shared Pool không dùng để xử lý dữ liệu truy xuất (việc xử lý dữ liệu thực hiện trong PGA hoặc Data Buffer Cache). Shared Pool chuyên dùng để lưu trữ thông tin dùng chung: mã SQL/PL-SQL (Library cache) và siêu dữ liệu từ điển dữ liệu (Data dictionary cache).",
    "key_takeaway_vi": "Shared Pool = Library Cache + Data Dictionary Cache, cấu hình qua SHARED_POOL_SIZE.",
    "flashcard_front_vi": "Mục đích chính của Shared Pool là gì?",
    "flashcard_back_vi": "Chia sẻ mã lệnh SQL (Library Cache) và định nghĩa bảng/quyền (Data Dictionary Cache) giữa các người dùng."
}

DATA_MOD_1_3[12] = {
    "prompt_vi": "Hệ thống nào sau đây đòi hỏi phải có một cơ sở dữ liệu (database)?",
    "options_vi": {
        "A": "Hệ thống tính lương (Payroll System).",
        "B": "Hệ thống đặt vé máy bay (Airline reservations system).",
        "C": "Một trang web lưu trữ người dùng đăng ký.",
        "D": "Tất cả các hệ thống trên (All of the above)."
    },
    "explanation_vi": "Bất kỳ hệ thống nào cần lưu trữ dữ liệu an toàn, xử lý đồng thời, truy vấn nhanh và đảm bảo tính toàn vẹn (tính lương, đặt vé, lưu tài khoản người dùng) đều bắt buộc cần một hệ thống quản trị cơ sở dữ liệu.",
    "key_takeaway_vi": "Tất cả các hệ thống quản lý thông tin nghiệp vụ và giao dịch đều cần DBMS.",
    "flashcard_front_vi": "Hệ thống nào cần dùng Database?",
    "flashcard_back_vi": "Tất cả: Hệ thống bảng lương, đặt chỗ máy bay, quản lý tài khoản web."
}

DATA_MOD_1_3[13] = {
    "prompt_vi": "Thành phần nào sau đây KHÔNG NẰM TRONG vùng nhớ Program Global Area (PGA)?",
    "options_vi": {
        "A": "Kế hoạch thực thi SQL (SQL Execution Plan).",
        "B": "Thông tin phiên làm việc (Session information).",
        "C": "Thông tin con trỏ (Cursor information).",
        "D": "Vùng làm việc thực thi SQL (SQL execution work areas - Sort/Hash)."
    },
    "explanation_vi": "Kế hoạch thực thi (SQL Execution Plan) được lưu trong Library Cache (thuộc SGA) để mọi phiên làm việc có thể tái sử dụng. PGA là vùng nhớ riêng cho từng tiến trình người dùng, chỉ lưu trạng thái con trỏ (Cursor state), thông tin phiên và vùng làm việc tạm thời.",
    "key_takeaway_vi": "Execution Plan nằm trong SGA (Library Cache). PGA chỉ lưu Session info, Cursor state, Work areas.",
    "flashcard_front_vi": "Kế hoạch thực thi (SQL Execution Plan) nằm ở SGA hay PGA?",
    "flashcard_back_vi": "Nằm trong SGA (Library Cache thuộc Shared Pool) để các phiên làm việc có thể dùng chung."
}

DATA_MOD_1_3[14] = {
    "prompt_vi": "Khái niệm nào sau đây KHÔNG PHẢI là một mức trừu tượng hợp lệ trong kiến trúc DBMS?",
    "options_vi": {
        "A": "Bảng (Tables).",
        "B": "Khung nhìn (Views / External Schema).",
        "C": "Lược đồ khái niệm (Conceptual Schema).",
        "D": "Lược đồ vật lý (Physical Schema)."
    },
    "explanation_vi": "Theo kiến trúc 3 mức chuẩn ANSI/SPARC, 3 mức trừu tượng hóa dữ liệu là: 1. External/View Level (Mức khung nhìn); 2. Conceptual Level (Mức khái niệm); 3. Internal/Physical Level (Mức vật lý). 'Tables' chỉ là cấu trúc lưu trữ cụ thể trong mô hình quan hệ, không phải tên mức trừu tượng.",
    "key_takeaway_vi": "3 mức trừu tượng hóa: Mức Ngoài/Khung nhìn (View), Mức Khái niệm (Conceptual), Mức Vật lý (Physical).",
    "flashcard_front_vi": "3 mức trừu tượng của hệ CSDL theo chuẩn ANSI/SPARC là gì?",
    "flashcard_back_vi": "View/External level (Mức nhìn), Conceptual level (Mức khái niệm), Physical/Internal level (Mức vật lý)."
}

DATA_MOD_1_3[15] = {
    "prompt_vi": "Đặc trưng nào sau đây KHÔNG THUỘC các thuộc tính ACID của một giao dịch (Transaction)?",
    "options_vi": {
        "A": "Tính độc lập (Independence).",
        "B": "Tính nguyên tố (Atomicity).",
        "C": "Tính nhất quán (Consistency).",
        "D": "Tính bền vững (Durability)."
    },
    "explanation_vi": "ACID gồm 4 thuộc tính: Atomicity (Tính nguyên tố - tất cả hoặc không gì cả), Consistency (Tính nhất quán), Isolation (Tính cô lập), Durability (Tính bền vững). Không có thuộc tính nào tên là 'Independence'.",
    "key_takeaway_vi": "Thuộc tính ACID: A = Atomicity, C = Consistency, I = Isolation, D = Durability.",
    "flashcard_front_vi": "Chữ I trong ACID là viết tắt của từ gì?",
    "flashcard_back_vi": "Isolation (Tính cô lập), không phải Independence."
}

DATA_MOD_1_3[16] = {
    "prompt_vi": "Đâu là những ưu điểm của DBMS so với hệ thống tệp truyền thống (File System)?",
    "options_vi": {
        "A": "Tất cả các ưu điểm trên (All of the above).",
        "B": "Khả năng tạo các báo cáo dữ liệu (Data Reports).",
        "C": "Truy vấn dữ liệu hiệu quả cao (Efficient Querying).",
        "D": "Khớp và sắp xếp dữ liệu (Matching and Sorting)."
    },
    "explanation_vi": "DBMS vượt trội hơn File System ở mọi khía cạnh xử lý dữ liệu: cung cấp ngôn ngữ truy vấn cấp cao (SQL), tối ưu hóa sắp xếp và lọc dữ liệu, quản lý tính toàn vẹn và hỗ trợ kết xuất báo cáo nhanh chóng.",
    "key_takeaway_vi": "DBMS vượt trội File System ở năng lực truy vấn, sắp xếp, lọc, báo cáo và kiểm soát truy cập đồng thời.",
    "flashcard_front_vi": "Ưu điểm của DBMS so với hệ thống tệp?",
    "flashcard_back_vi": "Truy vấn dữ liệu tối ưu, lọc và sắp xếp tự động, tạo báo cáo dễ dàng, đảm bảo toàn vẹn dữ liệu."
}

DATA_MOD_1_3[17] = {
    "prompt_vi": "Thuật ngữ nào sau đây KHÔNG PHẢI là một loại hệ quản trị cơ sở dữ liệu hợp lệ?",
    "options_vi": {
        "A": "OODBMS (Operations Oriented Database Management System)",
        "B": "NDBMS (Networked Database Management System)",
        "C": "HDBMS (Hierarchical Database Management System)",
        "D": "RDBMS (Relational Database Management System - trong đề in nhầm 'unsigned charRDBMS')"
    },
    "explanation_vi": "OODBMS thực chất là 'Object-Oriented Database Management System' (Hệ quản trị CSDL hướng đối tượng). Khái niệm 'Operations Oriented' là thuật ngữ sai được bịa ra trong đề thi.",
    "key_takeaway_vi": "OODBMS là Object-Oriented DBMS. Không có loại CSDL 'Operations Oriented'.",
    "flashcard_front_vi": "OODBMS viết tắt chuẩn là gì?",
    "flashcard_back_vi": "Object-Oriented Database Management System."
}

DATA_MOD_1_3[18] = {
    "prompt_vi": "Thành phần nào sau đây KHÔNG PHẢI là một phần của Cơ sở dữ liệu Oracle (Oracle Database vật lý)?",
    "options_vi": {
        "A": "Shared Pool",
        "B": "Data Files",
        "C": "Control Files",
        "D": "Redo Log Files"
    },
    "explanation_vi": "Trong kiến trúc Oracle: Oracle Database (vật lý) chỉ gồm các tệp đĩa: Data files, Control files, và Redo log files. Shared Pool là cấu trúc bộ nhớ trên RAM thuộc về Oracle Instance.",
    "key_takeaway_vi": "Database = Datafiles + Control files + Redo log files (đĩa). Shared Pool thuộc về Instance (RAM).",
    "flashcard_front_vi": "Phân biệt Oracle Database và Oracle Instance?",
    "flashcard_back_vi": "Database = Các tệp lưu trên đĩa; Instance = Bộ nhớ RAM (SGA) + Tiến trình nền (Background Processes)."
}

DATA_MOD_1_3[19] = {
    "prompt_vi": "Trong một hệ thống, nhiều ________ có thể chia sẻ một vùng nhớ SGA? (Theo ngữ cảnh đề thi)",
    "options_vi": {
        "A": "Server Processes (Tiến trình máy chủ)",
        "B": "PMON Processes",
        "C": "Instances",
        "D": "Databases"
    },
    "explanation_vi": "⚠️ LƯU Ý GIẢNG VIÊN: Trong kiến trúc máy tính, SGA là vùng nhớ chia sẻ mà nhiều Server Processes cùng truy cập. Tuy nhiên, đáp án trong ngân hàng đề CDAC đánh dấu C (Instances). Theo chuẩn kỹ thuật Oracle: Các Server Processes chia sẻ một SGA; còn nhiều Instances thì chia sẻ một Database (Oracle RAC). Học viên cần nắm rõ cả thực tế kiến trúc và đáp án ngân hàng đề.",
    "key_takeaway_vi": "Server Processes chia sẻ bộ nhớ SGA của Instance. Đi thi CDAC chú ý đáp án ngân hàng câu hỏi.",
    "flashcard_front_vi": "Các Server Process trong Oracle dùng chung vùng nhớ nào?",
    "flashcard_back_vi": "Dùng chung vùng nhớ SGA (System Global Area)."
}

DATA_MOD_1_3[20] = {
    "prompt_vi": "Thành phần nào sau đây KHÔNG THUỘC vùng nhớ System Global Area (SGA)?",
    "options_vi": {
        "A": "Vùng sắp xếp (Sort Area)",
        "B": "Database Buffer Cache",
        "C": "Library Cache",
        "D": "Shared Pool"
    },
    "explanation_vi": "Vùng sắp xếp (Sort Area) thuộc bộ nhớ riêng tư PGA (Program Global Area) của tiến trình người dùng, không thuộc SGA.",
    "key_takeaway_vi": "Sort Area thuộc vùng nhớ PGA riêng của từng phiên, không thuộc SGA dùng chung.",
    "flashcard_front_vi": "Sort Area thuộc vùng nhớ nào?",
    "flashcard_back_vi": "Thuộc PGA (Program Global Area), không nằm trong SGA."
}

# MODULE 2: Introduction to SQL (Q21 - Q40)
DATA_MOD_1_3[21] = {
    "prompt_vi": "Từ viết tắt SQL là viết tắt của cụm từ nào?",
    "options_vi": {
        "A": "Structured Query Language (Ngôn ngữ truy vấn có cấu trúc)",
        "B": "Structured Question Language",
        "C": "Strong Question Language",
        "D": "Strong Query Language"
    },
    "explanation_vi": "SQL là viết tắt của 'Structured Query Language' (Ngôn ngữ truy vấn có cấu trúc), do IBM phát triển và được ANSI/ISO chuẩn hóa để giao tiếp với các hệ quản trị cơ sở dữ liệu quan hệ.",
    "key_takeaway_vi": "SQL = Structured Query Language.",
    "flashcard_front_vi": "SQL là viết tắt của gì?",
    "flashcard_back_vi": "Structured Query Language (Ngôn ngữ truy vấn có cấu trúc)."
}

DATA_MOD_1_3[22] = {
    "prompt_vi": "Bảng Employee có các cột:\nEmpno Number(4)\nEname Varchar2(10)\njob varchar2(10)\nsal Varchar2(10)\nBạn cần hiển thị thông tin nhân viên bằng truy vấn sau:\nSELECT Empno, Ename, Job \"Employee Information\" FROM employee;\nSau khi thực thi câu truy vấn, kết quả sẽ hiển thị bao nhiêu cột?",
    "options_vi": {
        "A": "2 cột",
        "B": "1 cột (Theo đáp án trắc nghiệm đề gốc đánh dấu 100)",
        "C": "3 cột",
        "D": "0 cột"
    },
    "explanation_vi": "⚠️ LƯU Ý KỸ THUẬT & ĐỀ THI: Trong câu lệnh `SELECT Empno, Ename, Job \"Employee Information\" FROM employee;`, có 3 biểu thức cột được chọn: `Empno`, `Ename`, và `Job` (được gán alias là 'Employee Information'). Kết quả thực tế khi chạy trên Oracle là 3 CỘT. Tuy nhiên, đáp án trắc nghiệm trong file CDAC chấm phương án B (1 cột) - có thể người soạn đề nhầm lẫn câu hỏi hoặc coi alias như gom nhóm. Sinh viên cần lưu ý: Khi thi trắc nghiệm theo đúng bộ đề CDAC này chọn B, nhưng đi làm thực tế và phỏng vấn thì chắc chắn là 3 cột!",
    "key_takeaway_vi": "Thực tế câu lệnh SELECT có 3 cột (Empno, Ename, Job với bí danh). Đề thi CDAC chấm đáp án B.",
    "flashcard_front_vi": "SELECT Empno, Ename, Job \"Employee Information\" hiển thị bao nhiêu cột?",
    "flashcard_back_vi": "Thực tế hiển thị 3 cột riêng biệt. (Lưu ý đề thi CDAC có lỗi chấm đáp án 1 cột)."
}

DATA_MOD_1_3[23] = {
    "prompt_vi": "Bảng ITEM có các cột: ITEM_ID NUMBER(9), COST NUMBER(7,2), RETAIL NUMBER(7,2). Các cột RETAIL và COST đều chứa giá trị lớn hơn 0.\nĐánh giá 2 câu lệnh SQL sau:\n1. SELECT item_id, (retail * 1.25) + 5.00 - (cost * 1.10) - (cost * .10) AS Calculated Profit FROM item;\n2. SELECT item_id, retail * 1.25 + 5.00 - cost * 1.10 - cost * .10 \"Calculated Profit\" FROM item;\nKết quả sẽ như thế nào?",
    "options_vi": {
        "A": "Một trong hai câu lệnh sẽ KHÔNG THỂ thực thi (One of the statements will NOT execute).",
        "B": "Câu lệnh 1 sẽ hiển thị tiêu đề cột là 'Calculated Profit'.",
        "C": "Câu lệnh 1 và câu lệnh 2 sẽ trả về cùng một giá trị kết quả.",
        "D": "Câu lệnh 1 sẽ trả về giá trị cao hơn câu lệnh 2."
    },
    "explanation_vi": "Câu lệnh 1 bị lỗi cú pháp vì đặt bí danh cột có khoảng trắng `AS Calculated Profit` mà KHÔNG CÓ dấu ngoặc kép đôi `\"Calculated Profit\"`. Trong Oracle SQL, nếu bí danh chứa khoảng trắng thì bắt buộc phải bọc trong cặp ngoặc kép. Do đó câu lệnh 1 sẽ báo lỗi ORA-00923, không thể thực thi được!",
    "key_takeaway_vi": "Bí danh cột chứa dấu cách bắt buộc phải bọc trong dấu ngoặc kép đôi (\" \"). Thiếu ngoặc kép sẽ gây lỗi cú pháp.",
    "flashcard_front_vi": "Tại sao 'AS Calculated Profit' gây lỗi cú pháp trong SQL?",
    "flashcard_back_vi": "Vì bí danh chứa dấu cách bắt buộc phải đặt trong dấu ngoặc kép: AS \"Calculated Profit\"."
}

DATA_MOD_1_3[24] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây tạo bí danh Annual Salary (có dấu cách) cho cột tính toán SALARY*12?",
    "options_vi": {
        "A": "SELECT ename, salary*12 AS INITCAP ('ANNUAL SALARY') FROM employees;",
        "B": "SELECT ename, salary*12 AS Annual Salary FROM employees;",
        "C": "SELECT ename, salary*12 Annual Salary FROM employees;",
        "D": "SELECT ename, salary*12 'Annual Salary' FROM employees; (Hoặc \"Annual Salary\")"
    },
    "explanation_vi": "Để đặt bí danh chứa khoảng cách, cú pháp chuẩn Oracle yêu cầu dấu nháy kép `\"Annual Salary\"`. Trong SQL*Plus truyền thống, một số phiên bản chấp nhận nháy đơn cho bí danh, và đáp án trong đề thi CDAC chọn phương án D.",
    "key_takeaway_vi": "Bí danh có dấu cách cần dấu nháy (nháy kép chuẩn SQL ANSI/Oracle: \"Annual Salary\"). Đề thi CDAC chọn D.",
    "flashcard_front_vi": "Khi đặt bí danh cột có khoảng cách trong SQL cần lưu ý gì?",
    "flashcard_back_vi": "Bắt buộc phải đặt trong dấu nháy kép \" \". Trong đề CDAC ghi nhận phương án D."
}

DATA_MOD_1_3[25] = {
    "prompt_vi": "Đánh giá câu lệnh SQL: SELECT ename, sal, 12*sal+100 FROM emp;\nCột SAL lưu lương tháng. Thay đổi nào sau đây cần thực hiện để tính tổng thu nhập năm theo công thức 'lương tháng cộng tiền thưởng hàng tháng 100$, tất cả nhân với 12'?",
    "options_vi": {
        "A": "SELECT ename, sal, 12*(sal+100) FROM emp;",
        "B": "Không cần thay đổi gì.",
        "C": "SELECT ename, sal, (12*sal) +100 FROM emp;",
        "D": "SELECT ename, sal+100,*12 FROM emp;"
    },
    "explanation_vi": "Quy tắc ưu tiên toán tử trong SQL: Phép nhân (*) có độ ưu tiên cao hơn phép cộng (+). Do đó, biểu thức `12*sal+100` sẽ tính `(12*sal) + 100`. Để tính lương tháng cộng 100 rồi mới nhân 12, ta bắt buộc phải dùng dấu ngoặc đơn: `12*(sal+100)`.",
    "key_takeaway_vi": "Toán tử trong ngoặc đơn () luôn được ưu tiên tính trước phép nhân và phép cộng.",
    "flashcard_front_vi": "Làm sao để ép phép cộng thực hiện trước phép nhân trong SQL?",
    "flashcard_back_vi": "Sử dụng dấu ngoặc đơn: 12 * (sal + 100)."
}

DATA_MOD_1_3[26] = {
    "prompt_vi": "Bạn cần tạo kết quả hiển thị dòng chữ \"Dear Customer customer_name, \". Dữ liệu customer_name lấy từ cột CUSTOMER_NAME trong bảng CUSTOMERS. Câu lệnh nào sau đây tạo ra kết quả này?",
    "options_vi": {
        "A": "SELECT 'Dear Customer ' customer_name ',' FROM customers; (Theo định dạng đề thi CDAC)",
        "B": "SELECT dear customer, customer_name, FROM customers;",
        "C": "SELECT \"Dear Customer\", customer_name ',' FROM customers;",
        "D": "SELECT 'Dear Customer ' customer_name ',' FROM customers;"
    },
    "explanation_vi": "Trong Oracle SQL, chuỗi ký tự cố định được bọc trong dấu nháy đơn `'Dear Customer '`. Lưu ý chuẩn Oracle thường dùng toán tử nối chuỗi `||` (`'Dear Customer ' || customer_name || ', '`), nhưng trong bài trắc nghiệm CDAC, các biểu thức chuỗi được liệt kê thành các cột riêng biệt.",
    "key_takeaway_vi": "Chuỗi hằng số trong SQL bắt buộc phải đặt trong dấu nháy đơn '...'. Dấu nháy kép \"...\" chỉ dùng cho định danh/bí danh.",
    "flashcard_front_vi": "Chuỗi hằng ký tự trong SQL được đặt trong dấu nháy nào?",
    "flashcard_back_vi": "Dấu nháy đơn ' ' (Single quotes). Dấu nháy kép \" \" dùng cho Column Alias."
}

DATA_MOD_1_3[27] = {
    "prompt_vi": "Câu truy vấn nào sau đây hiển thị chính xác mỗi dòng của bảng Employees duy nhất một lần (loại bỏ các dòng trùng lặp hoàn toàn)?",
    "options_vi": {
        "A": "SELECT distinct * from employees;",
        "B": "SELECT unique rows from employees;",
        "C": "SELECT * from employees;",
        "D": "SELECT distinct rows from employees;"
    },
    "explanation_vi": "Từ khóa `DISTINCT` đứng ngay sau `SELECT` sẽ loại bỏ tất cả các dòng trùng lặp trong tập kết quả trả về. `SELECT DISTINCT *` sẽ kiểm tra sự trùng lặp trên tất cả các cột của bảng.",
    "key_takeaway_vi": "Loại bỏ dòng trùng lặp trong SQL dùng: SELECT DISTINCT * FROM ...",
    "flashcard_front_vi": "Từ khóa nào dùng để loại bỏ các hàng trùng lặp trong câu lệnh SELECT?",
    "flashcard_back_vi": "DISTINCT (đặt ngay sau SELECT: SELECT DISTINCT ...)."
}

DATA_MOD_1_3[28] = {
    "prompt_vi": "Kết quả xuất ra của câu lệnh truy vấn sau là gì?\nSELECT 1 FROM employees;",
    "options_vi": {
        "A": "Câu lệnh sẽ trả về giá trị 1 với số lần xuất hiện bằng đúng số lượng dòng có trong bảng employees.",
        "B": "Câu lệnh sẽ chỉ trả về dòng đầu tiên của bảng employees.",
        "C": "Câu lệnh sẽ chỉ trả về duy nhất một dòng và một cột có giá trị là 1.",
        "D": "Câu lệnh sẽ báo lỗi cú pháp."
    },
    "explanation_vi": "Mệnh đề `SELECT hằng_số FROM bảng` sẽ duyệt qua từng dòng của bảng và với mỗi dòng thỏa mãn, nó trả về giá trị hằng số đó. Vì không có điều kiện WHERE, bảng `employees` có bao nhiêu dòng thì câu lệnh sẽ trả về bấy nhiêu dòng có giá trị 1.",
    "key_takeaway_vi": "SELECT 1 FROM table trả về N dòng mang số 1, với N là số lượng bản ghi của bảng.",
    "flashcard_front_vi": "SELECT 1 FROM employees trả về kết quả gì?",
    "flashcard_back_vi": "Trả về số 1 cho mỗi dòng hiện có trong bảng employees (số dòng trả về = tổng số dòng trong bảng)."
}

DATA_MOD_1_3[29] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về câu lệnh SQL?",
    "options_vi": {
        "A": "Các mệnh đề (clauses) bắt buộc phải được viết trên các dòng riêng biệt.",
        "B": "Các câu lệnh SQL không phân biệt chữ hoa chữ thường (case-insensitive).",
        "C": "Câu lệnh SQL có thể được viết trên một hoặc nhiều dòng.",
        "D": "Các từ khóa (keywords) không được viết tắt hoặc ngắt đôi sang dòng khác."
    },
    "explanation_vi": "Phát biểu A là sai vì SQL là ngôn ngữ tự do (free-format). Bạn hoàn toàn có thể viết toàn bộ câu lệnh SELECT trên một dòng duy nhất mà không gây lỗi (việc chia dòng chỉ để tăng tính thẩm mỹ và dễ đọc).",
    "key_takeaway_vi": "SQL là free-format, không bắt buộc mệnh đề phải ở dòng riêng, từ khóa không phân biệt hoa thường.",
    "flashcard_front_vi": "SQL có bắt buộc mỗi mệnh đề (SELECT, FROM, WHERE) phải ở một dòng riêng không?",
    "flashcard_back_vi": "KHÔNG. Có thể viết toàn bộ câu lệnh SQL trên một dòng liên tục."
}

DATA_MOD_1_3[30] = {
    "prompt_vi": "Điều nào sau đây là ĐÚNG khi nói về giá trị NULL trong SQL?",
    "options_vi": {
        "A": "NULL là một giá trị chưa có, chưa được gán, không xác định hoặc không áp dụng được.",
        "B": "NULL tương đương với chuỗi khoảng trắng (blank spaces).",
        "C": "NULL trong một cột kiểu số (number) có thể được tự động coi là số 0.",
        "D": "NULL biểu thị một giá trị bị sai (incorrect value)."
    },
    "explanation_vi": "Trong mô hình quan hệ và SQL, `NULL` không phải là số 0, không phải là chuỗi rỗng `''`, và không phải là khoảng trắng. `NULL` đại diện cho một trạng thái dữ liệu: không có sẵn (unavailable), chưa gán (unassigned), chưa biết (unknown) hoặc không áp dụng được (inapplicable).",
    "key_takeaway_vi": "NULL là trạng thái không xác định/chưa có, KHÔNG BẰNG số 0, KHÔNG BẰNG chuỗi rỗng.",
    "flashcard_front_vi": "NULL trong SQL có bằng 0 hoặc khoảng trắng không?",
    "flashcard_back_vi": "KHÔNG. NULL đại diện cho giá trị chưa biết (unknown), chưa được gán hoặc không áp dụng."
}

DATA_MOD_1_3[31] = {
    "prompt_vi": "Kết quả của biểu thức sau sẽ là gì đối với những nhân viên có commission_pct là NULL?\nSELECT 12 * salary * commission_pct 'ANNSAL_COMM' FROM employees;",
    "options_vi": {
        "A": "Không câu nào ở trên đúng.",
        "B": "Bằng 0.",
        "C": "Bằng NULL.",
        "D": "Không thể dự đoán được (Unpredictable)."
    },
    "explanation_vi": "Quy tắc vàng trong SQL: Bất kỳ phép toán số học nào (+, -, *, /) thực hiện với giá trị NULL đều sẽ trả về kết quả là NULL. Vì `commission_pct` là NULL nên `12 * salary * NULL` sẽ cho kết quả là `NULL`.",
    "key_takeaway_vi": "Bất kỳ phép tính số học nào chứa NULL đều trả về NULL.",
    "flashcard_front_vi": "Phép tính: 12 * salary * NULL cho kết quả là gì?",
    "flashcard_back_vi": "Kết quả là NULL. Mọi phép toán số học với NULL đều bằng NULL."
}

DATA_MOD_1_3[32] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây được dùng để trích xuất (truy vấn) dữ liệu từ cơ sở dữ liệu?",
    "options_vi": {
        "A": "SELECT",
        "B": "GET",
        "C": "OPEN",
        "D": "EXTRACT"
    },
    "explanation_vi": "Câu lệnh `SELECT` là câu lệnh cơ bản thuộc nhóm DQL (Data Query Language) dùng để đọc và trích xuất dữ liệu từ một hoặc nhiều bảng trong cơ sở dữ liệu.",
    "key_takeaway_vi": "Lệnh trích xuất dữ liệu trong SQL là SELECT.",
    "flashcard_front_vi": "Lệnh trích xuất dữ liệu từ bảng là lệnh gì?",
    "flashcard_back_vi": "SELECT."
}

DATA_MOD_1_3[33] = {
    "prompt_vi": "Phát biểu nào sau đây về bí danh cột (Column Alias) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Bắt buộc phải dùng từ khóa \"AS\" ở giữa tên cột và bí danh.",
        "B": "Bí danh cột giúp đổi tên tiêu đề hiển thị của cột trong kết quả truy vấn.",
        "C": "Bí danh cột yêu cầu dấu ngoặc kép đôi nếu nó chứa khoảng trắng, ký tự đặc biệt hoặc cần phân biệt hoa thường.",
        "D": "Bí danh cột phải đứng ngay sau tên cột."
    },
    "explanation_vi": "Từ khóa `AS` là tùy chọn (optional) trong SQL, không bắt buộc. Ví dụ `SELECT salary sal` hoàn toàn tương đương với `SELECT salary AS sal`.",
    "key_takeaway_vi": "Từ khóa AS khi đặt bí danh cột là tùy chọn (không bắt buộc).",
    "flashcard_front_vi": "Từ khóa AS khi đặt bí danh cột có bắt buộc không?",
    "flashcard_back_vi": "KHÔNG bắt buộc. Có thể viết: column_name alias hoặc column_name AS alias."
}

DATA_MOD_1_3[34] = {
    "prompt_vi": "Trong SQL, câu lệnh nào sau đây chọn cột \"FirstName\" từ bảng có tên là \"Persons\"?",
    "options_vi": {
        "A": "SELECT Persons.FirstName ;",
        "B": "SELECT FirstName FROM Persons;",
        "C": "EXTRACT FirstName FROM Persons ;",
        "D": "SELECT FROM persons the FirstName;"
    },
    "explanation_vi": "Cú pháp cơ bản chuẩn của SQL là: `SELECT <danh_sách_cột> FROM <tên_bảng>;`. Do đó câu lệnh chính xác là `SELECT FirstName FROM Persons;`.",
    "key_takeaway_vi": "Cú pháp chuẩn: SELECT column_name FROM table_name;",
    "flashcard_front_vi": "Cú pháp lấy 1 cột từ 1 bảng trong SQL?",
    "flashcard_back_vi": "SELECT column_name FROM table_name;"
}

DATA_MOD_1_3[35] = {
    "prompt_vi": "Trong câu truy vấn sau, biểu thức nào được ưu tiên tính toán trước?\nSELECT id_number, (quantity - 100 / 0.15 + 20 - 10) FROM inventory",
    "options_vi": {
        "A": "20 - 10",
        "B": "0.15 + 20",
        "C": "100 / 0.15",
        "D": "quantity - 100"
    },
    "explanation_vi": "Bên trong dấu ngoặc đơn `(quantity - 100 / 0.15 + 20 - 10)`, quy tắc ưu tiên toán tử số học là phép nhân và chia (*, /) được thực hiện trước phép cộng và trừ (+, -). Do đó phép chia `100 / 0.15` sẽ được tính toán đầu tiên.",
    "key_takeaway_vi": "Thứ tự ưu tiên toán tử: Dấu ngoặc () -> Phép nhân/chia (*, /) -> Phép cộng/trừ (+, -).",
    "flashcard_front_vi": "Trong biểu thức (a - b / c + d), phép tính nào tính trước?",
    "flashcard_back_vi": "Phép chia b / c được ưu tiên tính trước vì nhân/chia có thứ tự ưu tiên cao hơn cộng/trừ."
}

DATA_MOD_1_3[36] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây được dùng để chỉ trả về các giá trị phân biệt (loại bỏ giá trị trùng nhau)?",
    "options_vi": {
        "A": "SELECT DISTINCT",
        "B": "SELECT DIFFERENT",
        "C": "SELECT UNIQUE",
        "D": "SELECT NO DUPLICATES"
    },
    "explanation_vi": "Từ khóa chuẩn SQL ANSI để lọc các giá trị không trùng lặp là `DISTINCT`. (Mặc dù Oracle cũng hỗ trợ từ khóa đồng nghĩa `UNIQUE`, nhưng `DISTINCT` là cú pháp chuẩn quốc tế ANSI SQL được khuyến nghị và là đáp án chuẩn của bài thi).",
    "key_takeaway_vi": "Từ khóa lọc giá trị khác nhau duy nhất là SELECT DISTINCT.",
    "flashcard_front_vi": "Từ khóa chuẩn SQL lọc dữ liệu không trùng lặp là gì?",
    "flashcard_back_vi": "SELECT DISTINCT."
}

DATA_MOD_1_3[37] = {
    "prompt_vi": "Những mệnh đề nào trong câu lệnh SELECT là bắt buộc phải có khi truy vấn từ một bảng trong Oracle?",
    "options_vi": {
        "A": "SELECT và FROM",
        "B": "Chỉ SELECT",
        "C": "SELECT và WHERE",
        "D": "SELECT, FROM và WHERE"
    },
    "explanation_vi": "Trong Oracle SQL, một câu lệnh truy vấn dữ liệu bắt buộc phải có ít nhất 2 mệnh đề: `SELECT` (chỉ định các cột/biểu thức cần lấy) và `FROM` (chỉ định bảng hoặc nguồn dữ liệu, kể cả khi tính toán biểu thức cũng phải `FROM dual`).",
    "key_takeaway_vi": "SELECT và FROM là hai mệnh đề bắt buộc trong câu lệnh truy vấn cơ sở dữ liệu.",
    "flashcard_front_vi": "Hai mệnh đề bắt buộc phải có trong câu lệnh SELECT của Oracle là gì?",
    "flashcard_back_vi": "SELECT và FROM."
}

DATA_MOD_1_3[38] = {
    "prompt_vi": "Câu lệnh SELECT nào sau đây hiển thị các cặp kết hợp duy nhất giữa giá trị POSITION và MANAGER từ bảng EMPLOYEE?",
    "options_vi": {
        "A": "SELECT position, manager DISTINCT FROM employee;",
        "B": "SELECT DISTINCT position, manager FROM employee;",
        "C": "SELECT position, manager FROM employee;",
        "D": "SELECT position, DISTINCT manager FROM employee;"
    },
    "explanation_vi": "Từ khóa `DISTINCT` luôn luôn phải đứng ngay sau từ khóa `SELECT` và nó áp dụng cho toàn bộ tổ hợp các cột được liệt kê phía sau (`DISTINCT position, manager`), chứ không thể đặt ở giữa danh sách cột hay sau tên cột.",
    "key_takeaway_vi": "DISTINCT phải đặt ngay sau SELECT: SELECT DISTINCT col1, col2 FROM ...",
    "flashcard_front_vi": "Từ khóa DISTINCT đặt ở vị trí nào trong câu lệnh SELECT nhiều cột?",
    "flashcard_back_vi": "Ngay sau từ khóa SELECT: SELECT DISTINCT col1, col2 FROM table."
}

DATA_MOD_1_3[39] = {
    "prompt_vi": "Khi soạn thảo truy vấn trong SQL*Plus, phát biểu nào sau đây mô tả đúng cách chỉ định bí danh cột (Column Alias)?",
    "options_vi": {
        "A": "Đặt bí danh ở cuối câu lệnh để mô tả bảng.",
        "B": "Đặt bí danh sau mỗi cột, ngăn cách bằng dấu phẩy.",
        "C": "Đặt bí danh sau mỗi cột, ngăn cách bằng một dấu cách (space).",
        "D": "Đặt bí danh ở đầu câu lệnh để mô tả bảng."
    },
    "explanation_vi": "Cú pháp đặt bí danh cột: `tên_cột [AS] bí_danh`. Tức là bí danh được đặt ngay sau tên cột và cách nhau bằng một khoảng trắng (dấu cách), có thể có hoặc không có từ khóa `AS`.",
    "key_takeaway_vi": "Bí danh cột đặt ngay sau tên cột, cách nhau bằng dấu cách.",
    "flashcard_front_vi": "Cách chỉ định bí danh cột trong SQL?",
    "flashcard_back_vi": "Đặt bí danh ngay sau tên cột, phân cách bằng dấu cách (có thể thêm từ khóa AS)."
}

DATA_MOD_1_3[40] = {
    "prompt_vi": "Trong SQL, làm thế nào để chọn tất cả các cột từ bảng có tên \"Persons\"?",
    "options_vi": {
        "A": "SELECT *.Persons",
        "B": "SELECT Persons",
        "C": "SELECT [all] FROM Persons",
        "D": "SELECT * FROM Persons"
    },
    "explanation_vi": "Ký tự đại diện dấu sao `*` (asterisk) đại diện cho tất cả các cột có trong bảng. Do đó cú pháp lấy toàn bộ các cột là `SELECT * FROM Persons;`.",
    "key_takeaway_vi": "SELECT * FROM table dùng để lấy tất cả các cột.",
    "flashcard_front_vi": "Ký tự nào đại diện cho 'tất cả các cột' trong câu lệnh SELECT?",
    "flashcard_back_vi": "Dấu sao (*) -> SELECT * FROM table."
}

# MODULE 3: DDL (Q41 - Q60)
DATA_MOD_1_3[41] = {
    "prompt_vi": "Lệnh TRUNCATE thực hiện thao tác gì trên bảng?",
    "options_vi": {
        "A": "Xóa bảng (Removes the table - Theo đáp án ngân hàng đề CDAC)",
        "B": "Xóa tất cả các dòng dữ liệu khỏi bảng (Removes all rows from a table)",
        "C": "Rút ngắn bảng còn 10 dòng",
        "D": "Xóa tất cả các cột khỏi bảng"
    },
    "explanation_vi": "⚠️ LƯU Ý GIẢNG VIÊN & ĐỀ THI: Về mặt bản chất kỹ thuật cơ sở dữ liệu: `TRUNCATE TABLE` xóa toàn bộ các dòng dữ liệu và giải phóng không gian lưu trữ (storage space), cấu trúc bảng vẫn còn nguyên vẹn; trong khi lệnh `DROP TABLE` mới là lệnh xóa hoàn toàn cấu trúc bảng. Tuy nhiên, trong đề thi trắc nghiệm CDAC này, đáp án A ('Removes the table') được gán 100 điểm. Sinh viên cần chú ý bẫy này: Khi làm bài kiểm tra CDAC chọn A, nhưng khi trả lời phỏng vấn kỹ thuật hoặc bài thi quốc tế (Oracle OCA/OCP) phải khẳng định TRUNCATE xóa toàn bộ dòng và giữ nguyên cấu trúc bảng!",
    "key_takeaway_vi": "Bản chất: TRUNCATE xóa toàn bộ dữ liệu và giải phóng bộ nhớ, giữ nguyên cấu trúc bảng. Đề CDAC chấm A.",
    "flashcard_front_vi": "Khác biệt bản chất giữa TRUNCATE và DROP TABLE?",
    "flashcard_back_vi": "TRUNCATE xóa toàn bộ dữ liệu + giải phóng vùng nhớ (giữ cấu trúc bảng). DROP TABLE xóa toàn bộ dữ liệu lẫn cấu trúc bảng."
}

DATA_MOD_1_3[42] = {
    "prompt_vi": "Phát biểu nào sau đây về các kiểu dữ liệu trong Oracle là ĐÚNG?",
    "options_vi": {
        "A": "Kiểu dữ liệu CHAR nên được sử dụng cho dữ liệu ký tự có độ dài cố định (fixed-length).",
        "B": "Kiểu dữ liệu TIMESTAMP là phần mở rộng của kiểu VARCHAR2.",
        "C": "Kiểu dữ liệu BLOB lưu trữ dữ liệu ký tự lên đến 4 gigabyte.",
        "D": "Kiểu dữ liệu VARCHAR2 lưu trữ dữ liệu ký tự lên đến 4 gigabyte."
    },
    "explanation_vi": "Kiểu dữ liệu `CHAR(n)` được thiết kế riêng cho chuỗi ký tự có độ dài cố định (nếu chuỗi ngắn hơn, Oracle tự động bù khoảng trắng). Phương án B sai vì TIMESTAMP là mở rộng của DATE; phương án C sai vì BLOB lưu nhị phân (Binary LOB), CLOB mới lưu ký tự; phương án D sai vì VARCHAR2 tối đa 4000 bytes trong SQL (hoặc 32767 bytes từ 12c), không phải 4GB.",
    "key_takeaway_vi": "CHAR dành cho chuỗi có độ dài cố định. VARCHAR2 dành cho chuỗi có độ dài thay đổi.",
    "flashcard_front_vi": "Khi nào nên dùng kiểu dữ liệu CHAR thay vì VARCHAR2?",
    "flashcard_back_vi": "Khi dữ liệu luôn có độ dài cố định (ví dụ: mã quốc gia 'VN', mã zip code, mã định danh cố định độ dài)."
}

DATA_MOD_1_3[43] = {
    "prompt_vi": "Bảng EMPLOYEES có các cột: LAST_NAME VARCHAR2(35), SALARY NUMBER(8,2), HIRE_DATE DATE.\nBạn muốn thêm giá trị mặc định cho cột SALARY bằng câu lệnh:\nALTER TABLE EMPLOYEES MODIFY (SALARY DEFAULT 5000);\nĐiều gì là ĐÚNG về câu lệnh ALTER của bạn?",
    "options_vi": {
        "A": "Việc thay đổi giá trị DEFAULT chỉ ảnh hưởng đến các thao tác chèn (INSERT) tiếp theo vào bảng.",
        "B": "Định nghĩa cột không thể sửa đổi để thêm giá trị DEFAULT.",
        "C": "Không thể thêm giá trị DEFAULT cho cột có kiểu dữ liệu NUMBER.",
        "D": "Tất cả các dòng hiện có giá trị NULL ở cột SALARY sẽ được tự động cập nhật thành 5000."
    },
    "explanation_vi": "Trong Oracle SQL, khi thay đổi hoặc thêm giá trị `DEFAULT` cho một cột, giá trị mặc định này CHỈ áp dụng cho các lệnh `INSERT` được thực hiện trong tương lai (sau thời điểm sửa). Các bản ghi đã tồn tại trước đó trong bảng hoàn toàn không bị ảnh hưởng.",
    "key_takeaway_vi": "Giá trị DEFAULT mới chỉ có hiệu lực cho các lần INSERT tiếp theo, không tự cập nhật dữ liệu cũ.",
    "flashcard_front_vi": "Thay đổi DEFAULT của một cột có cập nhật lại các dòng NULL cũ không?",
    "flashcard_back_vi": "KHÔNG. Giá trị DEFAULT chỉ áp dụng cho các bản ghi được INSERT sau thời điểm đó."
}

DATA_MOD_1_3[44] = {
    "prompt_vi": "Bảng COMMERCIALS hiện có 20000 dòng, cột DESCRIPTION hiện chứa tối đa 1000 byte. Bạn cần tăng độ rộng cột này lên tối đa 2000 byte kiểu ký tự biến đổi. Câu lệnh nào hợp lệ?",
    "options_vi": {
        "A": "ALTER TABLE commercials MODIFY (description VARCHAR2(2000));",
        "B": "ALTER TABLE commercials MODIFY (description CHAR2(2000));",
        "C": "ALTER TABLE commercials CHANGE (description CHAR2(2000));",
        "D": "ALTER TABLE commercials CHANGE (description VARCHAR2(2000));"
    },
    "explanation_vi": "Trong Oracle SQL, để thay đổi kích thước hoặc kiểu dữ liệu của một cột hiện có, ta dùng mệnh đề `ALTER TABLE <tên_bảng> MODIFY (<tên_cột> <kiểu_mới>)`. Oracle không dùng từ khóa `CHANGE` (đây là từ khóa của MySQL) và không có kiểu `CHAR2`.",
    "key_takeaway_vi": "Sửa cột trong Oracle dùng: ALTER TABLE ... MODIFY (col datatype);",
    "flashcard_front_vi": "Cú pháp thay đổi độ rộng cột trong Oracle SQL là gì?",
    "flashcard_back_vi": "ALTER TABLE table_name MODIFY (column_name datatype);"
}

DATA_MOD_1_3[45] = {
    "prompt_vi": "Đánh giá câu lệnh: DROP TABLE DEPT;\nPhát biểu nào sau đây là SAI về câu lệnh trên?",
    "options_vi": {
        "A": "Tất cả các khung nhìn (views) dựa trên bảng DEPT đều bị xóa (All views are deleted).",
        "B": "Bạn không thể rollback câu lệnh này.",
        "C": "Tất cả các giao dịch đang chờ (pending transactions) đều được tự động commit.",
        "D": "Tất cả các chỉ mục (indexes) dựa trên bảng DEPT đều bị xóa."
    },
    "explanation_vi": "Khi bạn DROP TABLE, các View được tạo dựa trên bảng đó KHÔNG BỊ XÓA (not deleted), mà chúng chỉ chuyển sang trạng thái không hợp lệ (`INVALID`). Nếu sau này bạn tạo lại bảng DEPT, View sẽ có thể hợp lệ trở lại. Các phát biểu B, C, D đều đúng vì DROP là lệnh DDL (tự động COMMIT ngầm định và xóa index liên quan). Do đó phát biểu A là SAI.",
    "key_takeaway_vi": "DROP TABLE không xóa các VIEW liên quan mà chỉ làm chúng bị INVALID.",
    "flashcard_front_vi": "Điều gì xảy ra với các View khi bảng gốc bị DROP?",
    "flashcard_back_vi": "Các View KHÔNG bị xóa; chúng chỉ bị đánh dấu trạng thái INVALID."
}

DATA_MOD_1_3[46] = {
    "prompt_vi": "Phát biểu nào sau đây mô tả đúng về kiểu dữ liệu ROWID?",
    "options_vi": {
        "A": "Một chuỗi thập lục phân (hexadecimal string) đại diện cho địa chỉ duy nhất của một dòng trong bảng.",
        "B": "Dữ liệu nhị phân lên đến 4 gigabyte.",
        "C": "Dữ liệu ký tự lên đến 4 gigabyte.",
        "D": "Dữ liệu nhị phân thô có độ dài thay đổi lên đến 2 gigabyte."
    },
    "explanation_vi": "`ROWID` là một kiểu dữ liệu đặc biệt và là cột giả (pseudocolumn) trong Oracle, chứa địa chỉ vật lý chính xác của dòng dữ liệu trên ổ đĩa (bao gồm mã đối tượng dữ liệu, số tệp dữ liệu, số khối dữ liệu và vị trí dòng trong khối). Nó được hiển thị dưới dạng chuỗi thập lục phân (base 64/hexadecimal).",
    "key_takeaway_vi": "ROWID là địa chỉ vật lý duy nhất của mỗi dòng trong bảng Oracle, dạng chuỗi thập lục phân.",
    "flashcard_front_vi": "ROWID trong Oracle đại diện cho điều gì?",
    "flashcard_back_vi": "Địa chỉ vật lý duy nhất của hàng trong khối dữ liệu trên đĩa (hexadecimal string)."
}

DATA_MOD_1_3[47] = {
    "prompt_vi": "Bạn vừa thực thi câu lệnh: ALTER TABLE marketing DROP COLUMN profit;\nKhi nào thì cột profit thực sự bị xóa khỏi cơ sở dữ liệu?",
    "options_vi": {
        "A": "Ngay lập tức sau khi thực thi câu lệnh (Immediately following statement execution).",
        "B": "Sau khi thực hiện lệnh Alter table drop unused columns.",
        "C": "Sau khi thực hiện lệnh Alter table set unused column.",
        "D": "Sau khi thực hiện lệnh Alter table modify."
    },
    "explanation_vi": "Lệnh `ALTER TABLE ... DROP COLUMN` là một câu lệnh DDL trực tiếp, nó sẽ lập tức xóa định nghĩa cột khỏi từ điển dữ liệu và thu hồi không gian bộ nhớ của cột đó ngay khi câu lệnh thực thi xong. (Chỉ khi dùng `SET UNUSED` thì cột mới bị ẩn và chờ lệnh `DROP UNUSED COLUMNS` sau).",
    "key_takeaway_vi": "Lệnh DROP COLUMN xóa cột ngay lập tức khi thực thi.",
    "flashcard_front_vi": "Lệnh ALTER TABLE ... DROP COLUMN có hiệu lực khi nào?",
    "flashcard_back_vi": "Ngay lập tức sau khi câu lệnh được thực thi thành công."
}

DATA_MOD_1_3[48] = {
    "prompt_vi": "Tên nào sau đây có thể là một tên bảng (table name) hợp lệ trong Oracle?",
    "options_vi": {
        "A": "Catch_#22",
        "B": "Number",
        "C": "1966_Invoices",
        "D": "#Invoices"
    },
    "explanation_vi": "Quy tắc đặt tên đối tượng (bảng, cột) trong Oracle: Phải bắt đầu bằng một chữ cái (A-Z), độ dài 1-30 ký tự (từ Oracle 12.2 là 128 ký tự), chỉ chứa chữ cái, số, dấu gạch dưới (_), $, # và KHÔNG ĐƯỢC trùng với từ khóa dành riêng (reserved words) của Oracle. 'Number' trùng từ khóa kiểu dữ liệu; '1966_Invoices' bắt đầu bằng số; '#Invoices' bắt đầu bằng ký tự đặc biệt. Do đó chỉ có `Catch_#22` là hợp lệ.",
    "key_takeaway_vi": "Tên bảng trong Oracle BẮT BUỘC phải bắt đầu bằng chữ cái và không được trùng từ khóa dành riêng.",
    "flashcard_front_vi": "Tên bảng trong Oracle có được bắt đầu bằng chữ số hoặc ký tự # không?",
    "flashcard_back_vi": "KHÔNG. Tên bảng phải bắt đầu bằng một chữ cái (A-Z)."
}

DATA_MOD_1_3[49] = {
    "prompt_vi": "Phát biểu nào sau đây mô tả hành vi mặc định khi bạn tạo một bảng mới (CREATE TABLE)?",
    "options_vi": {
        "A": "Bảng được tạo trong schema của chính bạn (created in your schema).",
        "B": "Bảng có thể truy cập được bởi tất cả người dùng trong hệ thống.",
        "C": "Bảng được tạo trong public schema.",
        "D": "Bảng được tạo trong DBA schema."
    },
    "explanation_vi": "Mặc định, khi một người dùng thực thi `CREATE TABLE <tên_bảng>`, bảng sẽ được tạo trong schema thuộc sở hữu của người dùng đó (`your schema`) và chỉ người tạo hoặc quản trị viên (DBA) mới có quyền truy cập, trừ khi được cấp quyền (GRANT) cho người khác.",
    "key_takeaway_vi": "Mặc định, bảng được tạo trong chính schema của user đang đăng nhập.",
    "flashcard_front_vi": "Khi tạo bảng mới, bảng mặc định thuộc về schema nào?",
    "flashcard_back_vi": "Thuộc về schema của chính người dùng thực thi lệnh (your schema)."
}

DATA_MOD_1_3[50] = {
    "prompt_vi": "Bạn cần sửa đổi bảng STUDENTS hiện đang rỗng để thêm khóa chính (primary key) trên cột STUDENT_ID. Câu lệnh nào thực hiện đúng tác vụ này?",
    "options_vi": {
        "A": "ALTER TABLE students ADD CONSTRAINT stud_id_pk PRIMARY KEY (student_id);",
        "B": "ALTER TABLE students ADD PRIMARY KEY student_id;",
        "C": "ALTER TABLE students ADD CONSTRAINT PRIMARY KEY (student_id);",
        "D": "ALTER TABLE students ADD CONSTRAINT stud_id_pk PRIMARY KEY student_id;"
    },
    "explanation_vi": "Cú pháp chuẩn để thêm ràng buộc khóa chính cấp bảng: `ALTER TABLE <tên_bảng> ADD [CONSTRAINT <tên_ràng_buộc>] PRIMARY KEY (<tên_cột>);`. Cột phải được đặt trong dấu ngoặc đơn `(student_id)` và có tên ràng buộc hợp lệ.",
    "key_takeaway_vi": "Cú pháp thêm khóa chính: ALTER TABLE table ADD CONSTRAINT pk_name PRIMARY KEY (column);",
    "flashcard_front_vi": "Cú pháp ALTER TABLE để thêm ràng buộc PRIMARY KEY có đặt tên?",
    "flashcard_back_vi": "ALTER TABLE table_name ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);"
}

DATA_MOD_1_3[51] = {
    "prompt_vi": "Đánh giá câu lệnh: TRUNCATE TABLE DEPT;\nPhát biểu nào sau đây là KHÔNG ĐÚNG về câu lệnh này?",
    "options_vi": {
        "A": "Nó giải phóng không gian lưu trữ được sử dụng bởi bảng (Theo đáp án trắc nghiệm đề gốc đánh dấu 100)",
        "B": "Nó không giải phóng không gian lưu trữ được sử dụng bởi bảng.",
        "C": "Bạn KHÔNG THỂ rollback việc xóa các dòng sau khi lệnh thực thi.",
        "D": "Bạn phải là chủ sở hữu bảng hoặc có quyền hệ thống DROP ANY TABLE để truncate bảng DEPT."
    },
    "explanation_vi": "⚠️ LƯU Ý KỸ THUẬT & ĐỀ THI: Trên thực tế, `TRUNCATE TABLE` CÓ giải phóng không gian lưu trữ (releases storage space - đưa High Water Mark về ban đầu), và không thể ROLLBACK. Câu hỏi hỏi 'Which statement is NOT true?', câu B ('It does not release storage space') mới thực sự là phát biểu SAI. Tuy nhiên, ngân hàng câu hỏi CDAC đã đánh dấu nhầm đáp án A (có thể do đảo phương án hoặc nhầm lẫn giữa TRUE và NOT TRUE). Sinh viên cần chú ý bẫy này khi làm bài thi CDAC!",
    "key_takeaway_vi": "TRUNCATE có giải phóng bộ nhớ và không thể rollback. Cần chú ý đáp án câu 51 trong đề gốc CDAC.",
    "flashcard_front_vi": "Lệnh TRUNCATE TABLE có thu hồi (giải phóng) không gian lưu trữ không?",
    "flashcard_back_vi": "CÓ. TRUNCATE giải phóng các extents về tablespace (ngoại trừ initial extent) và reset High Water Mark."
}

DATA_MOD_1_3[52] = {
    "prompt_vi": "Điều nào sau đây KHÔNG PHẢI là một quy tắc chuẩn để đặt tên bảng trong cơ sở dữ liệu Oracle?",
    "options_vi": {
        "A": "Phải bắt đầu bằng một chữ số hoặc một chữ cái (Must begin with either a number or a letter).",
        "B": "Phải có độ dài từ 1 đến 30 ký tự (trong các phiên bản trước 12.2).",
        "C": "Không được trùng với từ khóa dành riêng của Oracle Server.",
        "D": "Chỉ được chứa các ký tự A-Z, a-z, 0-9, _, $, và #."
    },
    "explanation_vi": "Quy tắc đặt tên của Oracle quy định: Tên bảng BẮT BUỘC PHẢI BẮT ĐẦU BẰNG CHỮ CÁI, tuyệt đối không được bắt đầu bằng chữ số (number). Vì vậy phương án A là phát biểu SAI.",
    "key_takeaway_vi": "Tên bảng bắt buộc phải bắt đầu bằng chữ cái, KHÔNG được bắt đầu bằng chữ số.",
    "flashcard_front_vi": "Tên bảng trong Oracle có được bắt đầu bằng chữ số không?",
    "flashcard_back_vi": "KHÔNG. Phải bắt đầu bằng một chữ cái (A-Z)."
}

DATA_MOD_1_3[53] = {
    "prompt_vi": "Câu lệnh CREATE TABLE nào sau đây là hợp lệ?",
    "options_vi": {
        "A": "CREATE TABLE EMP9$# AS (empid number(2)); (Theo cấu trúc đề thi)",
        "B": "CREATE TABLE EMP*123 AS (empid number(2));",
        "C": "CREATE TABLE PACKAGE AS (packid num(2));",
        "D": "CREATE TABLE EMP_TEST AS (empid number(2));"
    },
    "explanation_vi": "Tên bảng trong Oracle có thể chứa ký tự `$`, `#`, `_` và bắt đầu bằng chữ cái. Tên `EMP*123` sai vì chứa dấu sao `*`. `PACKAGE` là từ khóa dành riêng (reserved word của PL/SQL). Trong đề thi CDAC, phương án A được thiết kế để kiểm tra việc tên bảng có thể chứa ký tự đặc biệt hợp lệ `$#`.",
    "key_takeaway_vi": "Tên bảng có thể chứa: A-Z, 0-9, _, $, # và không được trùng từ khóa dành riêng.",
    "flashcard_front_vi": "Các ký tự đặc biệt nào được phép xuất hiện trong tên bảng Oracle?",
    "flashcard_back_vi": "Dấu gạch dưới (_), dấu đô la ($), và dấu thăng (#)."
}

DATA_MOD_1_3[54] = {
    "prompt_vi": "Kiểu dữ liệu DATETIME nào sau đây KHÔNG THỂ sử dụng khi định nghĩa cột bảng trong Oracle?",
    "options_vi": {
        "A": "INTERVAL MONTH TO DAY",
        "B": "TIMESTAMP",
        "C": "INTERVAL DAY TO SECOND",
        "D": "INTERVAL YEAR TO MONTH"
    },
    "explanation_vi": "Oracle chỉ hỗ trợ hai kiểu dữ liệu khoảng thời gian (Interval datatypes) là: `INTERVAL YEAR TO MONTH` (năm đến tháng) và `INTERVAL DAY TO SECOND` (ngày đến giây). Không tồn tại kiểu `INTERVAL MONTH TO DAY` vì số ngày trong một tháng không cố định (28, 29, 30 hoặc 31 ngày) nên không thể chuyển đổi tương đương chính xác.",
    "key_takeaway_vi": "Oracle chỉ có INTERVAL YEAR TO MONTH và INTERVAL DAY TO SECOND; không có INTERVAL MONTH TO DAY.",
    "flashcard_front_vi": "Hai kiểu INTERVAL hợp lệ trong Oracle là gì?",
    "flashcard_back_vi": "INTERVAL YEAR TO MONTH và INTERVAL DAY TO SECOND."
}

DATA_MOD_1_3[55] = {
    "prompt_vi": "Phát biểu nào sau đây về bảng (table) trong Oracle là ĐÚNG?",
    "options_vi": {
        "A": "Kích thước của bảng KHÔNG CẦN phải chỉ định khi tạo bảng (The size does NOT need to be specified).",
        "B": "Một bảng có thể có tối đa lên đến 10,000 cột.",
        "C": "Không thể tạo bảng trong khi người dùng khác đang sử dụng cơ sở dữ liệu.",
        "D": "Cấu trúc của bảng không thể sửa đổi khi bảng đang trực tuyến (online)."
    },
    "explanation_vi": "Khi tạo bảng trong Oracle, bạn không cần phải khai báo trước kích thước tổng của bảng; Oracle sẽ tự động cấp phát dung lượng theo các Extent khi dữ liệu được thêm vào. (Số cột tối đa của 1 bảng Oracle truyền thống là 1000 cột, không phải 10,000; bảng vẫn tạo và sửa online bình thường).",
    "key_takeaway_vi": "Khi tạo bảng không cần chỉ định kích thước; Oracle tự động cấp phát extent động.",
    "flashcard_front_vi": "Số cột tối đa của một bảng trong Oracle (trước bản 23c) là bao nhiêu?",
    "flashcard_back_vi": "Tối đa 1000 cột (không phải 10,000 cột)."
}

DATA_MOD_1_3[56] = {
    "prompt_vi": "Bảng employees hiện có 3000 bản ghi. Câu lệnh nào sau đây dùng để tăng độ rộng cột EMP_LNAME lên 25 ký tự?",
    "options_vi": {
        "A": "ALTER TABLE employee MODIFY emp_lname VARCHAR2(25);",
        "B": "Bạn KHÔNG THỂ tăng độ rộng của cột EMP_LNAME khi bảng đã có dữ liệu.",
        "C": "ALTER TABLE employee RENAME emp_lname VARCHAR2(25);",
        "D": "ALTER employee TABLE MODIFY COLUMN emp_lname VARCHAR2(25);"
    },
    "explanation_vi": "Trong Oracle SQL, bạn luôn có thể TĂNG độ rộng của một cột chuỗi (kể cả khi bảng đã có dữ liệu) bằng cú pháp: `ALTER TABLE <tên_bảng> MODIFY <tên_cột> VARCHAR2(độ_rộng_mới);`.",
    "key_takeaway_vi": "Có thể tăng độ rộng cột VARCHAR2 bất kỳ lúc nào bằng lệnh ALTER TABLE ... MODIFY.",
    "flashcard_front_vi": "Có thể tăng độ dài cột VARCHAR2 khi bảng đã có dữ liệu không?",
    "flashcard_back_vi": "CÓ. Luôn được phép tăng độ rộng. (Thu hẹp độ rộng chỉ được nếu dữ liệu hiện có thỏa mãn kích thước mới hoặc bảng rỗng)."
}

DATA_MOD_1_3[57] = {
    "prompt_vi": "Câu lệnh nào sau đây sẽ xóa vĩnh viễn toàn bộ dữ liệu, các chỉ mục và cả cấu trúc của bảng PO_DETAIL?",
    "options_vi": {
        "A": "DROP TABLE po_detail;",
        "B": "DELETE TABLE po_detail;",
        "C": "TRUNCATE TABLE po_detail;",
        "D": "ALTER TABLE po_detail SET UNUSED (po_num, po_line_id, product_id, quantity, unit_price);"
    },
    "explanation_vi": "Lệnh `DROP TABLE` xóa hoàn toàn bảng: cấu trúc bảng, toàn bộ dữ liệu, các chỉ mục (indexes) và quyền hạn (grants) liên quan đều bị xóa vĩnh viễn khỏi cơ sở dữ liệu. TRUNCATE và DELETE chỉ xóa dữ liệu, giữ nguyên cấu trúc.",
    "key_takeaway_vi": "DROP TABLE xóa cả cấu trúc bảng, dữ liệu và toàn bộ chỉ mục trên bảng đó.",
    "flashcard_front_vi": "Lệnh nào xóa cả cấu trúc lẫn dữ liệu và indexes của bảng?",
    "flashcard_back_vi": "DROP TABLE."
}

DATA_MOD_1_3[58] = {
    "prompt_vi": "Bảng Employees có cột MGR_ID hiện có kiểu số và đang chứa dữ liệu. Bạn cần sửa cột này để người dùng có thể nhập ký tự văn bản. Câu lệnh nào thực hiện được việc này?",
    "options_vi": {
        "A": "Bạn KHÔNG THỂ sửa kiểu dữ liệu của cột MGR_ID (You CANNOT modifies the data type).",
        "B": "ALTER employee MODIFY (mgr_id VARCHAR2(15));",
        "C": "ALTER TABLE employee MODIFY (mgr_id VARCHAR2(15));",
        "D": "ALTER employee TABLE MODIFY COLUMN (mgr_id VARCHAR2(15));"
    },
    "explanation_vi": "Trong Oracle, nếu một cột ĐÃ CHỨA DỮ LIỆU, bạn không thể thay đổi kiểu dữ liệu của nó sang một kiểu dữ liệu không tương thích (từ NUMBER sang VARCHAR2) trừ khi tất cả các giá trị trong cột đó đều là NULL hoặc bảng rỗng.",
    "key_takeaway_vi": "Không thể đổi kiểu dữ liệu (từ NUMBER sang VARCHAR2) khi cột đang chứa dữ liệu.",
    "flashcard_front_vi": "Có thể đổi kiểu dữ liệu cột từ NUMBER sang VARCHAR2 khi cột đã có dữ liệu không?",
    "flashcard_back_vi": "KHÔNG. Cột phải hoàn toàn rỗng (hoặc chỉ chứa NULL) mới được đổi sang kiểu dữ liệu không tương thích."
}

DATA_MOD_1_3[59] = {
    "prompt_vi": "Câu lệnh CREATE TABLE nào sau đây sẽ KHÔNG BỊ LỖI?",
    "options_vi": {
        "A": "CREATE TABLE time (time1 NUMBER(9));",
        "B": "CREATE TABLE date (time_id NUMBER(9));",
        "C": "CREATE TABLE time* (time_id NUMBER(9));",
        "D": "CREATE TABLE $time (time_id NUMBER(9));"
    },
    "explanation_vi": "`date` là từ khóa dành riêng cho kiểu dữ liệu DATE trong SQL; `time*` chứa ký tự cấm `*`; `$time` bắt đầu bằng dấu đô la (tên bảng bắt buộc phải bắt đầu bằng chữ cái). `time` là một định danh hợp lệ (trong Oracle kiểu thời gian là TIMESTAMP hoặc DATE, từ TIME không phải từ khóa cấm tạo bảng). Do đó câu lệnh A thực thi thành công.",
    "key_takeaway_vi": "Tên bảng phải bắt đầu bằng chữ cái, không chứa ký tự toán học như * và không trùng từ khóa.",
    "flashcard_front_vi": "Tại sao tên bảng $time hoặc time* bị lỗi trong Oracle?",
    "flashcard_back_vi": "Vì tên bảng không được bắt đầu bằng ký tự $ và không được chứa ký tự dấu sao (*)."
}

DATA_MOD_1_3[60] = {
    "prompt_vi": "Xét cấu trúc bảng PRODUCT (bảng hiện KHÔNG CÓ DỮ LIỆU):\nPRODUCT_ID NUMBER Primary Key, PRODUCT_NAME VARCHAR2(25), SUPPLIER_ID NUMBER, LIST_PRICE NUMBER(7,2).\nBạn cần giảm độ chính xác của cột LIST_PRICE xuống NUMBER(6,2) và đặt giá trị mặc định là 5.00$ khi chèn bản ghi mới mà không có giá trị LIST_PRICE. Câu lệnh nào đúng?",
    "options_vi": {
        "A": "ALTER TABLE product MODIFY (list_price NUMBER(6,2) DEFAULT 5);",
        "B": "ALTER TABLE product ADD OR REPLACE (list_price NUMBER(8,2) DEFAULT 5);",
        "C": "ALTER TABLE product MODIFY COLUMN (list_price NUMBER(6,2) DEFAULT '$5.00');",
        "D": "Bạn KHÔNG THỂ giảm kích thước của cột LIST_PRICE."
    },
    "explanation_vi": "Vì bảng PRODUCT hiện đang không có bản ghi nào (rỗng), bạn hoàn toàn có quyền giảm kích thước cột xuống `NUMBER(6,2)`. Cú pháp chuẩn của Oracle là `ALTER TABLE ... MODIFY (<tên_cột> NUMBER(6,2) DEFAULT 5);`.",
    "key_takeaway_vi": "Khi bảng rỗng, có thể giảm kích thước/độ chính xác của cột và thiết lập DEFAULT trong cùng lệnh MODIFY.",
    "flashcard_front_vi": "Khi nào được phép giảm độ chính xác (precision) của cột số NUMBER?",
    "flashcard_back_vi": "Khi bảng chưa có dữ liệu (rỗng) hoặc tất cả giá trị hiện có đều là NULL / thỏa mãn kích thước nhỏ hơn."
}

print(f"Loaded {len(DATA_MOD_1_3)} questions for Modules 1-3.")
