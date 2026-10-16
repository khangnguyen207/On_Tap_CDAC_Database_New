# -*- coding: utf-8 -*-
"""
Module 1-4 (Q1 - Q80) Generator
Translates and provides deep pedagogical lecturer explanations
"""

import json

def get_batch1_enrichments():
    # Keyed by q_id
    d = {}
    
    # Q1
    d[1] = {
        "prompt_vi": "Đặc điểm nào sau đây KHÔNG PHẢI là một ưu điểm của Hệ quản trị cơ sở dữ liệu (DBMS)?",
        "options_vi": {
            "A": "Tạo dữ liệu ứng dụng của người dùng (User application data creation).",
            "B": "Tính độc lập dữ liệu và truy cập hiệu quả.",
            "C": "Giảm thời gian phát triển ứng dụng.",
            "D": "Đảm bảo tính toàn vẹn và an toàn bảo mật dữ liệu."
        },
        "explanation_vi": "Trong kiến trúc hệ thống, DBMS chịu trách nhiệm lưu trữ, quản lý, bảo mật và cung cấp cơ chế truy xuất dữ liệu độc lập với tầng ứng dụng. Việc 'tạo dữ liệu nghiệp vụ của ứng dụng' là trách nhiệm của phần mềm ứng dụng người dùng (Application/Business logic), không phải là ưu điểm do DBMS cung cấp.",
        "key_takeaway_vi": "DBMS quản lý và bảo vệ dữ liệu (tính độc lập, toàn vẹn, bảo mật); dữ liệu ứng dụng do người dùng/ứng dụng sinh ra.",
        "flashcard_front_vi": "Vì sao 'User application data creation' KHÔNG PHẢI là ưu điểm của DBMS?",
        "flashcard_back_vi": "Vì việc tạo dữ liệu nghiệp vụ là trách nhiệm của ứng dụng người dùng, DBMS chỉ đóng vai trò lưu trữ, quản lý và đảm bảo an toàn/toàn vẹn dữ liệu."
    }

    # Q2
    d[2] = {
        "prompt_vi": "Tiến trình nền (Background process) nào trong Oracle sẽ cập nhật các bản ghi từ bộ đệm Redo Log Buffer vào các tệp Online Redo Log Files khi có lệnh COMMIT xảy ra?",
        "options_vi": {
            "A": "LGWR (Log Writer)",
            "B": "DBWn (Database Writer)",
            "C": "CKPT (Checkpoint)",
            "D": "CJQn (Coordinator Job Queue)"
        },
        "explanation_vi": "Tiến trình LGWR (Log Writer) chịu trách nhiệm ghi tuần tự các khối thay đổi (redo entries) từ vùng đệm Redo Log Buffer (trong SGA) xuống các tệp đĩa Online Redo Log Files. LGWR ghi khi: có lệnh COMMIT, khi bộ đệm đầy 1/3, hoặc định kỳ mỗi 3 giây.",
        "key_takeaway_vi": "Ghi Redo Log khi COMMIT = tiến trình LGWR (Log Writer).",
        "flashcard_front_vi": "Tiến trình nền nào ghi Redo Log Buffer xuống đĩa khi COMMIT?",
        "flashcard_back_vi": "LGWR (Log Writer). DBWn ghi khối dữ liệu dirty block xuống datafile; CKPT đồng bộ thông tin kiểm tra."
    }

    # Q3
    d[3] = {
        "prompt_vi": "Những tệp nào sau đây có thể thực hiện cơ chế nhân bản/ghép kênh (multiplexed) trong cơ sở dữ liệu Oracle?",
        "options_vi": {
            "A": "Data Files (Tệp dữ liệu)",
            "B": "Control Files (Tệp điều khiển)",
            "C": "Parameter Files (Tệp tham số)",
            "D": "Data Buffer Cache (Bộ đệm dữ liệu)"
        },
        "explanation_vi": "LƯU Ý GIẢNG VIÊN & ĐỀ THI: Trong cơ sở dữ liệu Oracle, Control Files và Online Redo Log Files có cơ chế Multiplexing (nhân đôi/nhân ba bản ghi trên nhiều đĩa vật lý để chống hỏng hóc). Datafiles không hỗ trợ multiplexing nội tại của Oracle mà phải dùng phần cứng (RAID) hoặc ASM. Tuy nhiên, trong đề thi trắc nghiệm gốc CDAC, đáp án được gán là A (Data Files) - có thể người ra đề có sự nhầm lẫn với câu hỏi 'Which files CANNOT be multiplexed?' hoặc tài liệu chuẩn của CDAC tính theo đáp án A. Học viên cần nhớ cả hai mặt: đi thi CDAC chọn A, nhưng phỏng vấn kỹ thuật Oracle DBA phải khẳng định Control Files và Redo Log Files mới là các tệp được Oracle multiplex!",
        "key_takeaway_vi": "Trong kiến trúc Oracle: Control Files & Redo Log Files được Oracle multiplex trực tiếp. Đi thi CDAC chú ý đáp án A (Data Files).",
        "flashcard_front_vi": "Cơ chế Multiplexing trong Oracle áp dụng cho các tệp nào?",
        "flashcard_back_vi": "Về mặt chuẩn kỹ thuật Oracle: Control Files và Redo Log Files được multiplex. (Lưu ý đáp án gốc đề thi CDAC đánh dấu Data Files)."
    }

    # Q4
    d[4] = {
        "prompt_vi": "Phát biểu nào sau đây về Data files (Tệp dữ liệu) là KHÔNG ĐÚNG?",
        "options_vi": {
            "A": "Một Data file chỉ có thể thuộc về duy nhất một Tablespace.",
            "B": "Mỗi Tablespace bắt buộc phải có ít nhất một Data file.",
            "C": "Duy trì nhật ký các thay đổi của cơ sở dữ liệu để phục vụ khôi phục (recovery).",
            "D": "Data file chứa dữ liệu cơ sở dữ liệu, bao gồm bảng, chỉ mục (indexes), các phân đoạn tạm thời (temp segments)..."
        },
        "explanation_vi": "Phát biểu C sai vì nhiệm vụ duy trì nhật ký thay đổi để phục hồi dữ liệu là của Redo Log Files và Archive Log Files, không phải của Data Files. Data Files dùng để lưu trữ dữ liệu thực tế (bảng, chỉ mục, dữ liệu người dùng).",
        "key_takeaway_vi": "Data files chứa dữ liệu bảng/index; Redo log files mới chứa nhật ký thay đổi để phục hồi.",
        "flashcard_front_vi": "Tệp nào lưu nhật ký thay đổi để khôi phục trong Oracle?",
        "flashcard_back_vi": "Redo Log Files, KHÔNG PHẢI Data Files."
    }

    # Q5
    d[5] = {
        "prompt_vi": "Phát biểu nào sau đây về tệp tham số khởi động của Oracle (init.ora) là KHÔNG ĐÚNG?",
        "options_vi": {
            "A": "Bọc trong dấu ngoặc kép bất kỳ giá trị tham số nào có chứa ký tự đặc biệt.",
            "B": "Tệp khởi tạo chỉ nên chứa các tham số và chú thích (comments).",
            "C": "Nhiều tham số có thể được chỉ định trên một dòng, ngăn cách nhau bằng dấu cách.",
            "D": "Các tham số phải được chỉ định theo một thứ tự định trước (predefined order)."
        },
        "explanation_vi": "Trong tệp PFILE (init.ora), các tham số cấu hình có thể xuất hiện theo bất kỳ thứ tự nào, Oracle đọc toàn bộ tệp khi khởi động instance mà không bắt buộc theo thứ tự định trước.",
        "key_takeaway_vi": "Tham số trong init.ora không cần sắp xếp theo thứ tự nhất định.",
        "flashcard_front_vi": "Tệp init.ora (PFILE) có bắt buộc thứ tự tham số không?",
        "flashcard_back_vi": "KHÔNG. Các tham số có thể đặt ở bất kỳ thứ tự nào."
    }

    # Q6
    d[6] = {
        "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về Oracle Instance?",
        "options_vi": {
            "A": "Oracle Instance cung cấp phương thức để truy cập vào cơ sở dữ liệu Oracle.",
            "B": "Oracle Instance là tập hợp dữ liệu được xử lý như một đơn vị, nơi lưu trữ và truy xuất các thông tin liên quan.",
            "C": "Oracle Instance chỉ có thể mở và sử dụng một cơ sở dữ liệu tại một thời điểm.",
            "D": "Oracle Instance bao gồm vùng nhớ SGA (System Global Area) và các tiến trình nền (background processes)."
        },
        "explanation_vi": "Khái niệm 'tập hợp dữ liệu được lưu trữ trên đĩa như một đơn vị...' là định nghĩa của Database (Cơ sở dữ liệu vật lý). Trong khi đó, Instance là cấu trúc bộ nhớ (SGA) và các tiến trình nền (Background Processes) trên RAM.",
        "key_takeaway_vi": "Oracle Instance = SGA (RAM) + Background Processes. Database = Tập hợp các tệp dữ liệu trên đĩa.",
        "flashcard_front_vi": "Oracle Instance gồm những thành phần nào?",
        "flashcard_back_vi": "Instance = Bộ nhớ dùng chung SGA + Các tiến trình nền (Background Processes). Không bao gồm tệp đĩa vật lý."
    }

    # Q7
    d[7] = {
        "prompt_vi": "Thành phần nào sau đây KHÔNG THUỘC vùng nhớ System Global Area (SGA)?",
        "options_vi": {
            "A": "Redo Log Buffer",
            "B": "Data Buffer Cache",
            "C": "Parameter Files (Tệp tham số)",
            "D": "Shared Pool"
        },
        "explanation_vi": "SGA là vùng nhớ dùng chung trên RAM của Oracle Instance, bao gồm: Database Buffer Cache, Shared Pool, Redo Log Buffer, Large Pool, Java Pool, Streams Pool. Còn Parameter Files (init.ora hoặc spfile.ora) là tệp vật lý lưu trên ổ đĩa OS, không thuộc SGA.",
        "key_takeaway_vi": "SGA gồm Buffer Cache, Shared Pool, Redo Log Buffer. Parameter Files nằm trên đĩa cứng.",
        "flashcard_front_vi": "SGA trong Oracle gồm những thành phần chính nào?",
        "flashcard_back_vi": "Database Buffer Cache, Shared Pool, Redo Log Buffer, Large Pool. Tệp tham số (init.ora) nằm trên đĩa, không nằm trong SGA."
    }

    # Q8
    d[8] = {
        "prompt_vi": "Phát biểu nào sau đây về vùng đệm dữ liệu (Data buffer cache) là KHÔNG ĐÚNG?",
        "options_vi": {
            "A": "Data buffer cache lưu trữ tập hợp các câu lệnh SQL được sử dụng gần đây nhất.",
            "B": "Data buffer cache lưu trữ dữ liệu được truy cập gần đây nhất.",
            "C": "Data buffer cache đọc và ghi dữ liệu đến/từ các tệp dữ liệu (data files).",
            "D": "Kích thước của mỗi bộ đệm trong Data buffer cache bằng với kích thước của một Oracle Block."
        },
        "explanation_vi": "Nơi lưu trữ các câu lệnh SQL đã phân tích (parse tree, execution plan) là Library Cache (thuộc Shared Pool). Data Buffer Cache chỉ lưu trữ các khối dữ liệu (data blocks) được đọc từ đĩa lên để phục vụ người dùng.",
        "key_takeaway_vi": "Data Buffer Cache lưu dữ liệu bảng/chỉ mục; Library Cache (Shared Pool) mới lưu câu lệnh SQL.",
        "flashcard_front_vi": "Data Buffer Cache lưu trữ gì trong Oracle?",
        "flashcard_back_vi": "Lưu các khối dữ liệu (data blocks) gần đây. Câu lệnh SQL được lưu ở Library Cache trong Shared Pool."
    }

    # Q9
    d[9] = {
        "prompt_vi": "Phát biểu nào sau đây về Redo Log Buffer là KHÔNG ĐÚNG?",
        "options_vi": {
            "A": "Tiến trình máy khách (Client process) trực tiếp ghi nhận các thay đổi vào redo log buffer.",
            "B": "Redo log buffer ghi lại các thay đổi được thực hiện đối với cơ sở dữ liệu.",
            "C": "Tiến trình máy chủ (Server process) ghi nhận các thay đổi vào redo log buffer.",
            "D": "Redo log buffer ghi lại khối dữ liệu bị thay đổi, vị trí thay đổi và giá trị mới."
        },
        "explanation_vi": "Trong mô hình kiến trúc Oracle, tiến trình Client (ứng dụng người dùng) gửi câu lệnh SQL qua mạng, và chính Server Process (tiến trình máy chủ đại diện cho user) mới là bên ghi các bản ghi redo vào Redo Log Buffer.",
        "key_takeaway_vi": "Server process ghi vào Redo Log Buffer, Client process không bao giờ can thiệp trực tiếp vào SGA.",
        "flashcard_front_vi": "Tiến trình nào ghi thay đổi vào Redo Log Buffer?",
        "flashcard_back_vi": "Server Process (tiến trình máy chủ). Client process không có quyền truy cập trực tiếp SGA."
    }

    # Q10
    d[10] = {
        "prompt_vi": "Thành phần nào sau đây KHÔNG ĐƯỢC lưu trữ trong Library Cache?",
        "options_vi": {
            "A": "Kết quả trả về của các câu lệnh SQL (Results of the SQL statements).",
            "B": "Văn bản gốc của câu lệnh SQL (Text of SQL statement).",
            "C": "Cây cú pháp: phiên bản đã biên dịch của câu lệnh (Parse Tree).",
            "D": "Kế hoạch thực thi (Execution Plan)."
        },
        "explanation_vi": "Library Cache chỉ lưu mã SQL, Cây cú pháp (Parse Tree) và Kế hoạch thực thi (Execution Plan) để tái sử dụng (Soft Parse). Kết quả của câu lệnh SQL (tập kết quả dữ liệu) không được lưu trong Library Cache (trong Oracle 11g trở đi có Result Cache riêng biệt, nhưng không nằm trong Library Cache).",
        "key_takeaway_vi": "Library Cache lưu: SQL text, Parse Tree, Execution Plan. Không lưu kết quả bảng dữ liệu.",
        "flashcard_front_vi": "Library Cache chứa những gì?",
        "flashcard_back_vi": "Văn bản câu lệnh SQL, Cây cú pháp (Parse Tree), Kế hoạch thực thi (Execution Plan). Không chứa kết quả dữ liệu trả về."
    }

    # Q11
    d[11] = {
        "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về vùng nhớ Shared Pool?",
        "options_vi": {
            "A": "Shared Pool có thể được sử dụng bởi nhiều câu lệnh SQL để xử lý dữ liệu được truy xuất.",
            "B": "Shared Pool là một phần của vùng nhớ SGA.",
            "C": "Shared Pool bao gồm Library cache và Data dictionary cache.",
            "D": "Kích thước của Shared Pool được định kích thước bởi tham số SHARED_POOL_SIZE trong init.ora."
        },
        "explanation_vi": "Shared Pool không dùng để xử lý dữ liệu truy xuất (việc xử lý dữ liệu và sắp xếp diễn ra trong PGA hoặc Data Buffer Cache). Shared Pool chuyên dùng để chia sẻ mã thực thi (Library Cache) và siêu dữ liệu (Data Dictionary Cache).",
        "key_takeaway_vi": "Shared Pool = Library Cache + Data Dictionary Cache, kích thước đặt bởi SHARED_POOL_SIZE.",
        "flashcard_front_vi": "Vùng nhớ Shared Pool gồm 2 thành phần chính nào?",
        "flashcard_back_vi": "Library Cache (lưu SQL/PL-SQL) và Data Dictionary Cache (lưu định nghĩa bảng, quyền, ràng buộc)."
    }

    # Q12
    d[12] = {
        "prompt_vi": "Hệ thống nào sau đây đòi hỏi phải có một cơ sở dữ liệu (database)?",
        "options_vi": {
            "A": "Hệ thống tính lương (Payroll System).",
            "B": "Hệ thống đặt vé máy bay (Airline reservations system).",
            "C": "Một trang web thu thập thông tin người dùng đăng ký.",
            "D": "Tất cả các hệ thống trên (All of the above)."
        },
        "explanation_vi": "Tất cả các hệ thống trên đều đòi hỏi lưu trữ dữ liệu có cấu trúc, đảm bảo tính toàn vẹn, giao dịch đồng thời và an toàn bảo mật, do đó đều cần cơ sở dữ liệu.",
        "key_takeaway_vi": "Mọi hệ thống có lưu trữ thông tin nghiệp vụ, người dùng và giao dịch đều cần DBMS.",
        "flashcard_front_vi": "Hệ thống nào cần Database?",
        "flashcard_back_vi": "Tất cả: Hệ thống bảng lương, đặt vé máy bay, ứng dụng web lưu tài khoản."
    }

    # Q13
    d[13] = {
        "prompt_vi": "Thành phần nào sau đây KHÔNG NẰM TRONG vùng nhớ Program Global Area (PGA)?",
        "options_vi": {
            "A": "Kế hoạch thực thi SQL (SQL Execution Plan).",
            "B": "Thông tin phiên làm việc (Session information).",
            "C": "Thông tin con trỏ (Cursor information).",
            "D": "Khu vực làm việc thực thi SQL (SQL execution work areas - ví dụ Sort area, Hash area)."
        },
        "explanation_vi": "Kế hoạch thực thi (SQL Execution Plan) được lưu chung trong Library Cache (thuộc SGA) để mọi phiên làm việc có thể dùng lại (Shared SQL). Vùng nhớ PGA là vùng nhớ riêng tư của từng tiến trình Server Process, chỉ chứa Cursor State, Session info và Work areas.",
        "key_takeaway_vi": "Execution Plan lưu ở SGA (Library Cache). PGA chỉ chứa Session info, Cursor state, Sort/Hash area.",
        "flashcard_front_vi": "Kế hoạch thực thi (Execution Plan) nằm ở SGA hay PGA?",
        "flashcard_back_vi": "Nằm trong SGA (cụ thể là Library Cache thuộc Shared Pool) để dùng chung giữa các user."
    }

    # Q14
    d[14] = {
        "prompt_vi": "Khái niệm nào sau đây KHÔNG PHẢI là một mức trừu tượng hợp lệ trong mô hình kiến trúc DBMS?",
        "options_vi": {
            "A": "Bảng (Tables).",
            "B": "Khung nhìn (Views / External Schema).",
            "C": "Lược đồ khái niệm (Conceptual Schema).",
            "D": "Lược đồ vật lý (Physical Schema)."
        },
        "explanation_vi": "Theo kiến trúc 3 mức ANSI/SPARC của DBMS, 3 mức trừu tượng là: Mức vật lý (Physical Schema), Mức khái niệm (Conceptual Schema), và Mức khung nhìn/ngoài (View / External Schema). 'Tables' chỉ là đối tượng lưu trữ cụ thể trong CSDL quan hệ, không phải tên của một mức trừu tượng.",
        "key_takeaway_vi": "3 mức trừu tượng dữ liệu: Mức Ngoài (View), Mức Khái niệm (Conceptual), Mức Vật lý (Physical).",
        "flashcard_front_vi": "3 mức trừu tượng dữ liệu theo chuẩn ANSI/SPARC là gì?",
        "flashcard_back_vi": "1. External/View Level (Khung nhìn) 2. Conceptual Level (Khái niệm) 3. Physical/Internal Level (Vật lý)."
    }

    # Q15
    d[15] = {
        "prompt_vi": "Tính chất nào sau đây KHÔNG THUỘC các thuộc tính ACID của một giao dịch (Transaction)?",
        "options_vi": {
            "A": "Tính độc lập (Independence).",
            "B": "Tính nguyên tố (Atomicity).",
            "C": "Tính nhất quán (Consistency).",
            "D": "Tính bền vững (Durability)."
        },
        "explanation_vi": "ACID viết tắt của: A - Atomicity (Nguyên tố), C - Consistency (Nhất quán), I - Isolation (Cô lập), D - Durability (Bền vững). Chữ I là 'Isolation', không phải 'Independence'.",
        "key_takeaway_vi": "Thuộc tính ACID của Transaction gồm: Atomicity, Consistency, Isolation, Durability.",
        "flashcard_front_vi": "Chữ I trong thuộc tính ACID viết tắt của từ gì?",
        "flashcard_back_vi": "Isolation (Tính cô lập giữa các giao dịch thực thi đồng thời), không phải Independence."
    }

    # Q16
    d[16] = {
        "prompt_vi": "Đâu là những ưu điểm của DBMS so với hệ thống tệp truyền thống về mặt năng lực xử lý?",
        "options_vi": {
            "A": "Tất cả các ưu điểm trên (All of the above).",
            "B": "Khả năng tạo các báo cáo dữ liệu (Data Reports).",
            "C": "Truy vấn dữ liệu hiệu quả cao (Efficient Querying).",
            "D": "Khớp và sắp xếp dữ liệu (Matching and Sorting)."
        },
        "explanation_vi": "DBMS cung cấp công cụ tối ưu hóa truy vấn, chỉ mục để tăng tốc độ tìm kiếm, gom nhóm, sắp xếp và trích xuất báo cáo vượt trội hơn hẳn việc quét tệp tuần tự của File System.",
        "key_takeaway_vi": "DBMS vượt trội File System ở khả năng truy vấn, sắp xếp, báo cáo và quản lý truy cập đồng thời.",
        "flashcard_front_vi": "Ưu điểm của DBMS so với File System thông thường?",
        "flashcard_back_vi": "Truy vấn dữ liệu nhanh (chỉ mục), sắp xếp & so khớp mạnh mẽ, tạo báo cáo dễ dàng và chống dư thừa dữ liệu."
    }

    # Q17
    d[17] = {
        "prompt_vi": "Thuật ngữ nào sau đây KHÔNG PHẢI là một loại hệ quản trị cơ sở dữ liệu hợp lệ?",
        "options_vi": {
            "A": "OODBMS (Operations Oriented Database Management System)",
            "B": "NDBMS (Network Database Management System)",
            "C": "HDBMS (Hierarchical Database Management System)",
            "D": "RDBMS (Relational Database Management System - trong đề gốc có lỗi in 'unsigned charRDBMS')"
        },
        "explanation_vi": "OODBMS thực chất là viết tắt của 'Object-Oriented Database Management System' (Hệ quản trị CSDL hướng đối tượng), chứ KHÔNG PHẢI 'Operations Oriented'. (Lưu ý: Phương án D trong đề thi gốc có lỗi in ấn dính chuỗi 'unsigned charRDBMS', đây là lỗi typo kinh điển của tài liệu CDAC khi sao chép từ code C sang Word).",
        "key_takeaway_vi": "OODBMS là Object-Oriented DBMS, không có loại nào là 'Operations Oriented'.",
        "flashcard_front_vi": "OODBMS viết tắt chuẩn là gì?",
        "flashcard_back_vi": "Object-Oriented Database Management System (CSDL hướng đối tượng)."
    }

    # Q18
    d[18] = {
        "prompt_vi": "Thành phần nào sau đây KHÔNG PHẢI là một phần của Cơ sở dữ liệu Oracle (Oracle Database vật lý)?",
        "options_vi": {
            "A": "Shared Pool",
            "B": "Data Files",
            "C": "Control Files",
            "D": "Redo Log Files"
        },
        "explanation_vi": "Trong kiến trúc Oracle: Oracle Database (CSDL vật lý) gồm 3 loại tệp chính lưu trên ổ đĩa: Data files, Control files, và Redo Log files. Shared Pool là thành phần bộ nhớ trong SGA trên RAM (thuộc về Instance, không phải Database).",
        "key_takeaway_vi": "Database = Data files + Control files + Redo log files (trên đĩa). Shared Pool thuộc về Instance (trên RAM).",
        "flashcard_front_vi": "Phân biệt Oracle Database và Oracle Instance?",
        "flashcard_back_vi": "Oracle Database gồm các tệp đĩa (Datafile, Control file, Redo log file). Oracle Instance gồm bộ nhớ RAM (SGA) và tiến trình nền."
    }

    # Q19
    d[19] = {
        "prompt_vi": "Trong một hệ thống, nhiều ________ có thể chia sẻ một vùng nhớ SGA? (Theo đề thi)",
        "options_vi": {
            "A": "Server Processes (Tiến trình máy chủ)",
            "B": "PMON Processes",
            "C": "Instances",
            "D": "Databases"
        },
        "explanation_vi": "LƯU Ý GIẢNG VIÊN & ĐỀ THI: Trong kiến trúc máy tính, SGA (System Global Area) là vùng nhớ chia sẻ mà nhiều Server Processes và Background Processes cùng truy cập. Tuy nhiên đề thi CDAC đánh dấu đáp án C (Instances) trong một số ngữ cảnh cụm hoặc lỗi đáp án. Theo chuẩn Oracle DBA: Các Server Processes chia sẻ một SGA; còn nhiều Instances thì chia sẻ một Database (Oracle RAC - Real Application Clusters). Học viên cần nắm vững: Trên thực tế các Server Process chia sẻ SGA.",
        "key_takeaway_vi": "SGA là vùng nhớ chia sẻ (Shared Memory) cho nhiều Server Processes và Background Processes của 1 instance.",
        "flashcard_front_vi": "Các tiến trình nào chia sẻ bộ nhớ SGA?",
        "flashcard_back_vi": "Các Server Processes và Background Processes cùng chia sẻ bộ nhớ SGA của Instance."
    }

    # Q20
    d[20] = {
        "prompt_vi": "Thành phần nào trong danh sách sau đây KHÔNG THUỘC vùng nhớ System Global Area (SGA)?",
        "options_vi": {
            "A": "Vùng sắp xếp (Sort Area)",
            "B": "Database Buffer Cache",
            "C": "Library Cache",
            "D": "Shared Pool"
        },
        "explanation_vi": "Vùng sắp xếp dữ liệu (Sort Area) thuộc về bộ nhớ riêng tư Program Global Area (PGA) của tiến trình người dùng, hoặc Temporary Tablespace trên đĩa khi thiếu RAM. Database Buffer Cache, Library Cache và Shared Pool đều nằm trong SGA.",
        "key_takeaway_vi": "Sort Area thuộc về PGA (bộ nhớ riêng), không thuộc SGA (bộ nhớ chung).",
        "flashcard_front_vi": "Sort Area nằm ở đâu trong kiến trúc bộ nhớ Oracle?",
        "flashcard_back_vi": "Nằm trong PGA (Program Global Area) của tiến trình phục vụ người dùng."
    }

    return d

print("Batch 1 definitions loaded.")
