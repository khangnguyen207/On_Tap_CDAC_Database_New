# -*- coding: utf-8 -*-
"""
Module 10 (Q181-Q200), Module 11 (Q201-Q220), Module 12 (Q221-Q240), Module 13 (Q241-Q260)
Comprehensive Bilingual Translations & Lecturer Explanations
"""

DATA_MOD_10_13 = {}

# MODULE 10: Advanced Sub Queries (Q181 - Q200)
DATA_MOD_10_13[181] = {
    "prompt_vi": "Phát biểu nào sau đây về các câu truy vấn con (Sub queries) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Truy vấn con (truy vấn trong) trả về một giá trị được câu lệnh cha sử dụng.",
        "B": "Truy vấn con là một câu lệnh SELECT được lồng bên trong một mệnh đề của câu lệnh SQL khác.",
        "C": "Sử dụng truy vấn con lồng nhau tương đương với việc thực hiện 2 câu truy vấn tuần tự và lấy kết quả của câu trong làm giá trị tìm kiếm cho câu ngoài.",
        "D": "Câu truy vấn ngoài luôn được thực thi trước rồi mới đến truy vấn con bên trong (Outer query is executed first and then inner)."
    },
    "explanation_vi": "Phát biểu D là SAI vì đối với truy vấn con thông thường (Non-correlated subquery), câu truy vấn con bên trong (Inner query) luôn luôn được thực thi TRƯỚC HẾT để lấy kết quả, sau đó kết quả đó mới được nạp vào câu truy vấn ngoài (Outer query). Chỉ trong Correlated Subquery thì câu ngoài mới điều khiển vòng lặp của câu trong.",
    "key_takeaway_vi": "Trong truy vấn con tiêu chuẩn, inner query luôn thực thi trước rồi outer query mới thực thi.",
    "flashcard_front_vi": "Trong Subquery tiêu chuẩn, câu nào chạy trước?",
    "flashcard_back_vi": "Inner query (truy vấn con) chạy trước để cung cấp dữ liệu cho Outer query (truy vấn cha)."
}

DATA_MOD_10_13[182] = {
    "prompt_vi": "Loại truy vấn con nào được sử dụng trong câu lệnh SQL sau?\nSELECT employee_id, last_name, (CASE WHEN department_id = (SELECT department_id FROM departments WHERE location_id = 1800) THEN 'Canada' ELSE 'USA' END) location FROM employees;",
    "options_vi": {
        "A": "Truy vấn con so sánh cặp (Pair-wise comparison sub-query)",
        "B": "Truy vấn con tương quan (Correlated sub query)",
        "C": "Khung nhìn nội tuyến (Inline sub query)",
        "D": "Truy vấn con vô hướng (Scalar Sub query)"
    },
    "explanation_vi": "`Scalar Subquery` (truy vấn con vô hướng) là câu truy vấn con trả về chính xác DUY NHẤT MỘT GIÁ TRỊ (1 cột và 1 dòng). Từ Oracle 8i trở đi, Scalar Subquery có thể được đặt ở bất kỳ nơi nào chấp nhận một biểu thức đơn (Expression), bao gồm cả danh sách SELECT và biểu thức CASE.",
    "key_takeaway_vi": "Scalar Subquery trả về duy nhất 1 giá trị (1 cột, 1 hàng) và có thể đứng ở bất kỳ vị trí biểu thức nào.",
    "flashcard_front_vi": "Scalar Subquery là gì?",
    "flashcard_back_vi": "Là truy vấn con trả về đúng 1 giá trị đơn (1 hàng, 1 cột), dùng được trong biểu thức SELECT hoặc CASE."
}

DATA_MOD_10_13[183] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về truy vấn con tương quan (Correlated sub Queries)?",
    "options_vi": {
        "A": "Truy vấn con tương quan được đánh giá một lần cho mỗi dòng dữ liệu được câu lệnh cha xử lý.",
        "B": "Câu lệnh cha có thể là SELECT, UPDATE, hoặc DELETE.",
        "C": "Truy vấn con tương quan chỉ được đánh giá một lần duy nhất cho toàn bộ câu lệnh cha (evaluated once for each parent statement).",
        "D": "Oracle thực thi correlated subquery khi subquery tham chiếu đến một cột thuộc bảng của câu truy vấn cha."
    },
    "explanation_vi": "Phát biểu C là SAI. Khác với truy vấn con độc lập chỉ chạy 1 lần duy nhất, `Correlated Subquery` bắt buộc phải chạy lặp lại N LẦN, tương ứng với mỗi dòng dữ liệu mà câu lệnh cha duyệt qua.",
    "key_takeaway_vi": "Correlated Subquery được thực thi lặp lại một lần cho mỗi dòng của câu truy vấn cha.",
    "flashcard_front_vi": "Correlated Subquery chạy bao nhiêu lần?",
    "flashcard_back_vi": "Chạy lặp lại cho TỪNG DÒNG dữ liệu mà câu truy vấn cha xử lý."
}

DATA_MOD_10_13[184] = {
    "prompt_vi": "Loại truy vấn con nào được sử dụng trong câu lệnh SQL sau?\nSELECT employee_id, last_name FROM employees e ORDER BY (SELECT department_name FROM departments d WHERE e.department_id = d.department_id);",
    "options_vi": {
        "A": "Pair-wise comparison sub-query",
        "B": "Correlated sub query (Truy vấn con tương quan)",
        "C": "Inline sub query",
        "D": "Non-pair wise comparison query"
    },
    "explanation_vi": "Bên trong mệnh đề ORDER BY, truy vấn con tham chiếu đến cột `e.department_id` của bảng `employees e` ở câu truy vấn cha (`WHERE e.department_id = d.department_id`). Bất kỳ truy vấn con nào tham chiếu đến cột của truy vấn cha đều là `Correlated Subquery` (truy vấn con tương quan).",
    "key_takeaway_vi": "Subquery tham chiếu cột của bảng ngoài (e.department_id) chính là Correlated Subquery.",
    "flashcard_front_vi": "Dấu hiệu nhận biết Correlated Subquery là gì?",
    "flashcard_back_vi": "Subquery có chứa cột tham chiếu ngược ra bảng ở câu lệnh cha (ví dụ e.department_id = d.department_id)."
}

DATA_MOD_10_13[185] = {
    "prompt_vi": "Toán tử EXISTS trả về giá trị gì khi câu truy vấn con bên trong không chọn được bản ghi nào (rỗng)?",
    "options_vi": {
        "A": "0",
        "B": "FALSE",
        "C": "TRUE",
        "D": "NULL"
    },
    "explanation_vi": "Toán tử `EXISTS` kiểm tra sự tồn tại của dữ liệu: Nó trả về `TRUE` nếu câu truy vấn con tìm thấy ít nhất một dòng thỏa mãn; và trả về `FALSE` nếu truy vấn con không tìm thấy dòng nào (kết quả rỗng). Toán tử EXISTS không bao giờ trả về NULL.",
    "key_takeaway_vi": "Toán tử EXISTS trả về TRUE nếu có ít nhất 1 dòng, trả về FALSE nếu tập kết quả rỗng.",
    "flashcard_front_vi": "Toán tử EXISTS trả về gì khi truy vấn con không tìm thấy bản ghi nào?",
    "flashcard_back_vi": "Trả về FALSE (không bao giờ trả về NULL hay 0)."
}

DATA_MOD_10_13[186] = {
    "prompt_vi": "Kết quả của câu truy vấn sau sẽ là gì?\nSELECT employee_id, last_name, job_id, department_id FROM employees outer\nWHERE EXISTS (SELECT 'X' FROM employees WHERE manager_id = outer.employee_id);",
    "options_vi": {
        "A": "Hiển thị nhân viên có ít nhất một cấp dưới có mã nhân viên là 'X'.",
        "B": "Hiển thị những nhân viên có ít nhất một nhân viên khác báo cáo trực tiếp cho họ (Display employees who have at least one person reporting to them).",
        "C": "Hiển thị nhân viên có ít nhất một người quản lý phân công cho họ.",
        "D": "Hiển thị nhân viên có ít nhất một cấp dưới tên là 'X'."
    },
    "explanation_vi": "Điều kiện `manager_id = outer.employee_id` kiểm tra xem có ai xem nhân viên này là sếp (manager) hay không. `SELECT 'X'` là quy ước chuẩn trong EXISTS (chỉ cần kiểm tra sự tồn tại của dòng, không quan tâm nội dung cột). Kết quả là tìm ra tất cả những ai ĐANG LÀM QUẢN LÝ (có ít nhất 1 cấp dưới).",
    "key_takeaway_vi": "EXISTS (SELECT 'X' ... WHERE manager_id = outer.emp_id) tìm các nhân viên đóng vai trò là quản lý.",
    "flashcard_front_vi": "Tại sao người ta hay viết SELECT 'X' hoặc SELECT 1 trong mệnh đề EXISTS?",
    "flashcard_back_vi": "Vì EXISTS chỉ kiểm tra có dòng tồn tại hay không, không lấy giá trị cột nên SELECT 'X' là tối ưu nhất."
}

DATA_MOD_10_13[187] = {
    "prompt_vi": "Câu truy vấn nào sau đây hiển thị tất cả các phòng ban HIỆN KHÔNG CÓ bất kỳ nhân viên nào?",
    "options_vi": {
        "A": "SELECT department_id, department_name FROM departments d WHERE NOT EXISTS (SELECT 'X' FROM employees WHERE department_id = d.department_id);",
        "B": "SELECT department_id, department_name FROM departments d WHERE EXISTS (SELECT 'X' FROM employees WHERE department_id = d.department_id);",
        "C": "SELECT department_id, department_name FROM departments d WHERE NOT EXISTS (SELECT 'X' FROM employees WHERE department_id = department_id);",
        "D": "SELECT department_id, department_name FROM departments d WHERE EXISTS (SELECT 'X' FROM employees WHERE department_id = department_id);"
    },
    "explanation_vi": "Toán tử `NOT EXISTS` kết hợp với điều kiện tương quan `department_id = d.department_id` sẽ lọc ra các phòng ban mà khi tìm trong bảng employees không trả về bất kỳ nhân viên nào (tức phòng ban trống).",
    "key_takeaway_vi": "Tìm các bản ghi không có phần tử con tương ứng dùng NOT EXISTS kết hợp điều kiện tương quan.",
    "flashcard_front_vi": "Cú pháp tìm phòng ban không có nhân viên dùng NOT EXISTS?",
    "flashcard_back_vi": "WHERE NOT EXISTS (SELECT 1 FROM employees WHERE department_id = d.department_id)."
}

DATA_MOD_10_13[188] = {
    "prompt_vi": "Xem câu lệnh Update dưới đây, đây là loại update nào?\nUPDATE employees e SET department_name = (SELECT department_name FROM departments d WHERE e.department_id = d.department_id);",
    "options_vi": {
        "A": "Inline Update",
        "B": "Correlated Update (Cập nhật tương quan)",
        "C": "Direct Update",
        "D": "Indirect Update"
    },
    "explanation_vi": "Vì subquery trong mệnh đề SET tham chiếu đến cột `e.department_id` của bảng đang được UPDATE (`employees e`), subquery này phải được tính toán lại cho từng dòng được cập nhật. Đây chính là định nghĩa của `Correlated Update`.",
    "key_takeaway_vi": "UPDATE dùng subquery tham chiếu đến bảng đang update là Correlated Update.",
    "flashcard_front_vi": "Correlated Update trong SQL là gì?",
    "flashcard_back_vi": "Là câu lệnh UPDATE có subquery tham chiếu đến dòng hiện tại của bảng đang được cập nhật."
}

DATA_MOD_10_13[189] = {
    "prompt_vi": "Câu lệnh nào sau đây là một truy vấn con tương quan (correlated sub query) để xóa chỉ những dòng từ bảng EMPLOYEES mà cũng tồn tại trong bảng EMP_HISTORY?",
    "options_vi": {
        "A": "DELETE FROM employees E WHERE employee_id IN (SELECT employee_id FROM employees E, emp_history H WHERE E.employee_id = H.employee_id);",
        "B": "DELETE FROM employees E WHERE employee_id = (SELECT employee_id FROM emp_history WHERE employee_id = E.employee_id);",
        "C": "DELETE FROM employees E WHERE employee_id IN (SELECT employee_id FROM emp_history H)",
        "D": "DELETE FROM employees E , emp_history H WHERE E.employee_id = H.employee_id;"
    },
    "explanation_vi": "Trong câu B, subquery lấy `FROM emp_history WHERE employee_id = E.employee_id` - nó trực tiếp tham chiếu tới bí danh `E` của câu lệnh DELETE cha. Khi có bản ghi khớp, subquery trả về `employee_id` bằng chính `E.employee_id` nên dòng đó bị xóa. Đây là câu lệnh correlated subquery hợp lệ.",
    "key_takeaway_vi": "Correlated subquery trong DELETE tham chiếu bí danh của bảng đang bị xóa (E.employee_id).",
    "flashcard_front_vi": "Cách viết Correlated Subquery trong lệnh DELETE?",
    "flashcard_back_vi": "DELETE FROM table1 T1 WHERE col = (SELECT col FROM table2 WHERE col = T1.col);"
}

DATA_MOD_10_13[190] = {
    "prompt_vi": "Điều nào sau đây là KHÔNG ĐÚNG khi nói về việc sử dụng mệnh đề WITH?",
    "options_vi": {
        "A": "Sử dụng mệnh đề WITH, bạn có thể định nghĩa một khối truy vấn trước khi sử dụng nó trong một câu truy vấn chính.",
        "B": "Mệnh đề WITH còn được gọi là mệnh đề tách thừa số truy vấn con (subquery_factoring_clause).",
        "C": "Mệnh đề WITH cho phép bạn tái sử dụng cùng một khối truy vấn trong câu lệnh SELECT khi nó xuất hiện nhiều hơn 1 lần trong truy vấn phức tạp.",
        "D": "Mệnh đề WITH, khác với Inline views, có thể tạo ra các khung nhìn vĩnh viễn và tái sử dụng được (create permanent and reusable views)."
    },
    "explanation_vi": "Phát biểu D là SAI hoàn toàn. Mệnh đề `WITH` (Common Table Expression - CTE) chỉ tạo ra các tập kết quả tạm thời trong bộ nhớ phục vụ duy nhất cho phiên thực thi của câu lệnh đó; nó TUYỆT ĐỐI KHÔNG TẠO RA các View vĩnh viễn (permanent views) trong cơ sở dữ liệu. Muốn tạo view vĩnh viễn bắt buộc phải dùng lệnh DDL `CREATE VIEW`.",
    "key_takeaway_vi": "Mệnh đề WITH (CTE) chỉ mang tính tạm thời trong câu lệnh truy vấn, không tạo ra view vĩnh viễn trên đĩa.",
    "flashcard_front_vi": "Mệnh đề WITH có tạo ra một View vĩnh viễn trong CSDL không?",
    "flashcard_back_vi": "KHÔNG. Mệnh đề WITH chỉ tạo khối dữ liệu tạm thời (CTE) trong phạm vi câu lệnh SELECT đó."
}

DATA_MOD_10_13[191] = {
    "prompt_vi": "Khi nào thì việc sử dụng mệnh đề WITH mang lại hiệu quả cao nhất?",
    "options_vi": {
        "A": "Khi câu truy vấn có quá nhiều bảng cần kết nối.",
        "B": "Khi sử dụng các truy vấn con Inline trong mệnh đề FROM.",
        "C": "Khi một câu truy vấn có nhiều lần tham chiếu đến cùng một khối truy vấn và có chứa các phép JOIN cùng hàm tổng hợp.",
        "D": "Khi dùng mệnh đề WITH để thay thế hoàn toàn các correlated subqueries để tăng tốc."
    },
    "explanation_vi": "Mệnh đề WITH phát huy tối đa sức mạnh khi cùng một khối tính toán logic phức tạp (gom nhóm, tính tổng/trung bình, join) được tái sử dụng nhiều lần ở các nhánh khác nhau của câu truy vấn chính. Oracle sẽ tối ưu bằng cách chỉ tính toán khối WITH đó một lần duy nhất và lưu tạm vào Global Temporary Table trên bộ nhớ.",
    "key_takeaway_vi": "Mệnh đề WITH hiệu quả nhất khi một khối truy vấn phức tạp được gọi lại nhiều lần trong cùng câu lệnh.",
    "flashcard_front_vi": "Lợi ích lớn nhất của mệnh đề WITH (Subquery Factoring) là gì?",
    "flashcard_back_vi": "Tối ưu hóa hiệu năng bằng cách chỉ tính toán khối truy vấn 1 lần dù nó được gọi lại nhiều lần trong câu lệnh."
}

DATA_MOD_10_13[192] = {
    "prompt_vi": "Trường hợp nào sau đây là một mục đích sử dụng hợp lệ của câu truy vấn con (sub-query)?",
    "options_vi": {
        "A": "Định nghĩa tập hợp các dòng được chèn vào bảng đích của câu lệnh INSERT hoặc CREATE TABLE.",
        "B": "Cung cấp giá trị cho các điều kiện trong các mệnh đề WHERE, HAVING, và START WITH của câu lệnh SELECT.",
        "C": "Tất cả các trường hợp trên (All of the above).",
        "D": "Định nghĩa một hoặc nhiều giá trị được gán cho các dòng hiện có trong câu lệnh UPDATE."
    },
    "explanation_vi": "Subquery là cấu trúc vô cùng linh hoạt trong SQL: dùng trong CREATE TABLE AS SELECT, INSERT INTO ... SELECT, cung cấp điều kiện lọc trong WHERE / HAVING / START WITH, và tính giá trị gán trong UPDATE SET.",
    "key_takeaway_vi": "Subquery có thể dùng trong mọi câu lệnh SELECT, INSERT, UPDATE, CREATE TABLE.",
    "flashcard_front_vi": "Các vị trí có thể sử dụng Subquery trong SQL?",
    "flashcard_back_vi": "SELECT (danh sách cột, WHERE, HAVING, FROM), INSERT (subquery), UPDATE (SET, WHERE), CREATE TABLE (AS)."
}

DATA_MOD_10_13[193] = {
    "prompt_vi": "Điều nào sau đây KHÔNG PHẢI là một lợi ích của việc sử dụng mệnh đề WITH (WITH Clause)?",
    "options_vi": {
        "A": "Nó tự động sắp xếp kết quả đầu ra của câu truy vấn (automatically sorts the output).",
        "B": "Nó chỉ tính toán khối lệnh một lần duy nhất, ngay cả khi khối đó xuất hiện nhiều lần trong truy vấn.",
        "C": "Nó có thể nâng cao hiệu năng của các câu truy vấn phức tạp.",
        "D": "Nó giúp câu truy vấn trở nên trong sáng, dễ đọc và dễ bảo trì hơn."
    },
    "explanation_vi": "Phát biểu A là SAI vì mệnh đề WITH hoàn toàn không có tính năng tự động sắp xếp kết quả. Nếu muốn sắp xếp, bạn bắt buộc phải chỉ định tường minh mệnh đề `ORDER BY` ở câu truy vấn cuối cùng.",
    "key_takeaway_vi": "Mệnh đề WITH không tự động sắp xếp kết quả; muốn sắp xếp phải dùng ORDER BY.",
    "flashcard_front_vi": "Mệnh đề WITH có tự động sắp xếp dữ liệu trả về không?",
    "flashcard_back_vi": "KHÔNG. Muốn sắp xếp bắt buộc phải có ORDER BY ở câu SELECT ngoài cùng."
}

DATA_MOD_10_13[194] = {
    "prompt_vi": "Hãy chỉ ra toán tử khác biệt (odd one) trong số các toán tử sau được dùng đi kèm với câu truy vấn con?",
    "options_vi": {
        "A": "=",
        "B": "ANY",
        "C": "ALL",
        "D": "IN"
    },
    "explanation_vi": "Toán tử `=` là toán tử so sánh đơn dòng (Single-row comparison operator - chỉ so sánh với 1 giá trị duy nhất). Trong khi đó, `ANY`, `ALL`, và `IN` đều là các toán tử so sánh nhiều dòng (Multiple-row comparison operators). Do đó toán tử `=` là phần tử khác biệt.",
    "key_takeaway_vi": "Dấu '=' là toán tử so sánh đơn dòng; IN, ANY, ALL là toán tử so sánh nhiều dòng.",
    "flashcard_front_vi": "Phân biệt toán tử '=' với các toán tử IN, ANY, ALL?",
    "flashcard_back_vi": "'=' chỉ nhận 1 giá trị duy nhất (Single-row). IN, ANY, ALL nhận cả một tập hợp nhiều dòng (Multi-row)."
}

DATA_MOD_10_13[195] = {
    "prompt_vi": "Câu truy vấn nào sau đây hiển thị chi tiết của tất cả nhân viên có mức lương thấp hơn mức lương trung bình của toàn bộ công ty?",
    "options_vi": {
        "A": "SELECT last_name, job_id, salary FROM employees WHERE salary < (SELECT AVG(salary) FROM employees GROUP BY Department_id);",
        "B": "SELECT last_name, job_id, salary FROM employees HAVING salary < (SELECT AVG(salary) FROM employees);",
        "C": "SELECT last_name, job_id, salary FROM employees WHERE salary ANY (SELECT AVG(salary) FROM employees GROUP BY department_id);",
        "D": "SELECT last_name, job_id, salary FROM employees WHERE salary < (SELECT AVG(salary) FROM employees);"
    },
    "explanation_vi": "Để tính lương trung bình toàn công ty, ta dùng subquery: `SELECT AVG(salary) FROM employees` (không có GROUP BY để tính trung bình chung). Sau đó ở câu ngoài dùng toán tử so sánh đơn dòng: `WHERE salary < (...)`. Phương án D là chính xác.",
    "key_takeaway_vi": "Lọc nhân viên lương < trung bình công ty: WHERE salary < (SELECT AVG(salary) FROM employees).",
    "flashcard_front_vi": "Cú pháp tìm nhân viên có lương nhỏ hơn trung bình toàn công ty?",
    "flashcard_back_vi": "SELECT * FROM employees WHERE salary < (SELECT AVG(salary) FROM employees);"
}

DATA_MOD_10_13[196] = {
    "prompt_vi": "Truy vấn con nhiều cột (multicolumn sub query) là gì?",
    "options_vi": {
        "A": "Không có loại truy vấn con nào là Multi-column subquery, chỉ có multi-row subquery.",
        "B": "Một câu truy vấn con chọn ra nhiều hơn một cột được gọi là multicolumn sub query (selects more than one column).",
        "C": "Là truy vấn con sử dụng các toán tử đơn dòng để so sánh.",
        "D": "Là truy vấn con sử dụng các lệnh DECODE để xử lý nhiều cột."
    },
    "explanation_vi": "Đúng như tên gọi của nó, `Multi-column Subquery` là một câu truy vấn con trả về danh sách từ 2 cột trở lên trong mệnh đề SELECT của nó để so sánh đồng thời nhiều thuộc tính với câu truy vấn cha.",
    "key_takeaway_vi": "Multi-column subquery là truy vấn con chọn ra nhiều hơn 1 cột trong mệnh đề SELECT của nó.",
    "flashcard_front_vi": "Thế nào là một Multi-column subquery?",
    "flashcard_back_vi": "Là câu truy vấn con trả về từ 2 cột trở lên trong mệnh đề SELECT."
}

DATA_MOD_10_13[197] = {
    "prompt_vi": "Kết quả của câu truy vấn con nhiều cột (so sánh cặp - pairwise) sau là gì?\nSELECT employee_id, manager_id, department_id FROM employees\nWHERE (manager_id, department_id) IN (SELECT manager_id, department_id FROM employees WHERE employee_id IN (178, 174));",
    "options_vi": {
        "A": "Hiển thị nhân viên có cùng người quản lý VÀ cùng phòng ban với nhân viên có mã 178 hoặc 174.",
        "B": "Hiển thị nhân viên có cùng người quản lý và cùng phòng ban với cả 178 và 174.",
        "C": "Hiển thị nhân viên có cùng người quản lý với 178 hoặc 174 HOẶC cùng phòng ban với 178 hoặc 174.",
        "D": "Câu lệnh này bị lỗi cú pháp."
    },
    "explanation_vi": "Đây là phép so sánh cặp (`Pairwise comparison`): Cặp giá trị `(manager_id, department_id)` của nhân viên phải KHỚP ĐỒNG THỜI với cặp `(manager_id, department_id)` của nhân viên 178 HOẶC cặp của nhân viên 174.",
    "key_takeaway_vi": "So sánh cặp (Pairwise): (col1, col2) IN (...) đòi hỏi các cột phải khớp theo đúng cặp giá trị kết hợp.",
    "flashcard_front_vi": "Pairwise comparison trong subquery là gì?",
    "flashcard_back_vi": "So sánh theo cặp đồng thời: (col1, col2) IN (SELECT col1, col2...) - cả 2 giá trị phải khớp cùng lúc trên một hàng."
}

DATA_MOD_10_13[198] = {
    "prompt_vi": "Kết quả của câu truy vấn so sánh không theo cặp (non-pairwise comparison) sau là gì?\nSELECT employee_id, manager_id, department_id FROM employees\nWHERE manager_id IN (SELECT manager_id FROM employees WHERE employee_id IN (174, 141))\nAND department_id IN (SELECT department_id FROM employees WHERE employee_id IN (174, 141))\nAND employee_id NOT IN (174, 141);",
    "options_vi": {
        "A": "Hiển thị nhân viên có cùng người quản lý và cùng phòng ban với nhân viên 178 hoặc 174.",
        "B": "Báo lỗi cú pháp.",
        "C": "Hiển thị nhân viên có cùng người quản lý và cùng phòng ban với nhân viên 178 và 174.",
        "D": "Hiển thị nhân viên có người quản lý trùng với quản lý của 178/174 (đề gốc in 178/174) và có phòng ban trùng với phòng ban của 178/174 độc lập nhau."
    },
    "explanation_vi": "Trong phép so sánh `Non-pairwise`: Điều kiện `manager_id IN (...)` và `department_id IN (...)` được đánh giá ĐỘC LẬP với nhau. Nhân viên có thể có người quản lý giống nhân viên 174, nhưng phòng ban lại giống nhân viên 141 thì vẫn được chọn. Đây là sự khác biệt then chốt giữa Non-pairwise và Pairwise.",
    "key_takeaway_vi": "Non-pairwise so sánh từng cột riêng rẽ độc lập; Pairwise so sánh kết hợp các cột theo cặp.",
    "flashcard_front_vi": "Khác biệt giữa Pairwise và Non-pairwise multi-column subquery?",
    "flashcard_back_vi": "Pairwise so sánh đồng thời các cột thành 1 bộ giá trị. Non-pairwise so sánh từng cột độc lập qua các mệnh đề AND."
}

DATA_MOD_10_13[199] = {
    "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về Khung nhìn nội tuyến (Inline Sub Queries)?",
    "options_vi": {
        "A": "Một subquery trong mệnh đề FROM của câu lệnh SELECT định nghĩa một nguồn dữ liệu chỉ dành riêng cho câu lệnh SELECT đó.",
        "B": "Một subquery trong mệnh đề FROM còn được gọi là một inline view.",
        "C": "Các inline views được tạo ra trong subquery có thể được tái sử dụng sau này bởi cùng truy vấn hoặc các truy vấn khác (can be used later).",
        "D": "Bạn có thể dùng subquery trong FROM tương tự như cách sử dụng view."
    },
    "explanation_vi": "Phát biểu C là SAI hoàn toàn. `Inline View` là đối tượng tạm thời, chỉ tồn tại trong thời gian câu lệnh SQL đang thực thi. Khi câu lệnh kết thúc, Inline View lập tức biến mất và KHÔNG THỂ tái sử dụng bởi bất kỳ câu truy vấn nào khác sau đó.",
    "key_takeaway_vi": "Inline View chỉ có vòng đời trong 1 câu lệnh, không thể lưu lại để dùng cho các truy vấn khác.",
    "flashcard_front_vi": "Inline View có thể tái sử dụng cho các câu truy vấn khác sau này không?",
    "flashcard_back_vi": "KHÔNG. Inline View tự động hủy ngay sau khi câu lệnh thực thi xong."
}

DATA_MOD_10_13[200] = {
    "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về các câu truy vấn con vô hướng (Scalar sub queries)?",
    "options_vi": {
        "A": "Truy vấn con nhiều cột so sánh 2 cột trở lên không đủ điều kiện là scalar subquery (Theo đáp án trắc nghiệm đề CDAC đánh dấu 100)",
        "B": "Giá trị của biểu thức scalar subquery chính là giá trị của mục được chọn trong SELECT của subquery.",
        "C": "Nếu subquery trả về 0 dòng, giá trị của biểu thức scalar subquery là NULL.",
        "D": "Một subquery trả về chính xác 1 giá trị cột từ 1 dòng được gọi là scalar subquery."
    },
    "explanation_vi": "Định nghĩa chuẩn của `Scalar Subquery`: là câu truy vấn con trả về đúng 1 giá trị đơn (1 hàng, 1 cột). Nếu trả về 0 dòng, kết quả là NULL. Nếu trả về nhiều hơn 1 dòng hoặc nhiều hơn 1 cột, Oracle sẽ báo lỗi không hợp lệ.",
    "key_takeaway_vi": "Scalar subquery chỉ trả về 1 dòng và 1 cột; nếu không có dòng nào thì trả về NULL.",
    "flashcard_front_vi": "Scalar Subquery trả về giá trị gì nếu không tìm thấy dòng nào?",
    "flashcard_back_vi": "Trả về giá trị NULL."
}

# MODULE 11: Views (Q201 - Q220)
DATA_MOD_10_13[201] = {
    "prompt_vi": "Trong kịch bản nào sau đây, phân tích TOP-N (TOP N analysis) là giải pháp tốt nhất?",
    "options_vi": {
        "A": "Bạn muốn xác định người có mức lương cao nhất trong tất cả nhân viên.",
        "B": "Bạn muốn tìm người quản lý đang giám sát số lượng nhân viên lớn nhất.",
        "C": "Bạn muốn xếp hạng 3 đại diện bán hàng hàng đầu bán được số lượng sản phẩm lớn nhất (rank the top three sales representatives).",
        "D": "Bạn muốn xác định nhân viên có thâm niên cao nhất công ty."
    },
    "explanation_vi": "Phân tích `Top-N Analysis` được sử dụng khi bạn cần lấy ra một tập hợp gồm `N` đối tượng đứng đầu hoặc đứng cuối theo một tiêu chí xếp hạng nhất định (ví dụ: top 3 nhân viên bán hàng tốt nhất, top 10 sản phẩm bán chạy nhất...).",
    "key_takeaway_vi": "Top-N Analysis chuyên dùng để xếp hạng và lấy ra N bản ghi đứng đầu hoặc đứng cuối.",
    "flashcard_front_vi": "Top-N Analysis dùng cho bài toán gì?",
    "flashcard_back_vi": "Lấy ra N bản ghi có giá trị cao nhất hoặc thấp nhất theo thứ bậc (ví dụ: Top 3 doanh số)."
}

DATA_MOD_10_13[202] = {
    "prompt_vi": "Xét cấu trúc view EMP_DEPT_VU (kết hợp các cột từ bảng EMPLOYEES và DEPARTMENTS).\nCâu lệnh SQL nào sau đây sinh ra lỗi?",
    "options_vi": {
        "A": "SELECT * FROM emp_dept_vu;",
        "B": "SELECT department_id, SUM(salary) FROM emp_dept_vu GROUP BY department_id;",
        "C": "SELECT department_id, job_id, AVG(salary) FROM emp_dept_vu GROUP BY department_id, job_id;",
        "D": "Không có câu lệnh nào sinh ra lỗi; tất cả đều hợp lệ (None of the statements produce an error; all are valid)."
    },
    "explanation_vi": "Một View (khung nhìn) có thể được truy vấn hoàn toàn giống hệt như một bảng thực tế (Table). Bạn có thể `SELECT *`, có thể gom nhóm `GROUP BY`, và có thể dùng các hàm nhóm (SUM, AVG) trên View một cách bình thường.",
    "key_takeaway_vi": "Có thể truy vấn, gom nhóm GROUP BY và dùng hàm nhóm trên View tương tự như bảng dữ liệu.",
    "flashcard_front_vi": "Có thể dùng GROUP BY và hàm nhóm SUM/AVG khi truy vấn từ một View không?",
    "flashcard_back_vi": "CÓ. View có thể được truy vấn bình thường như một bảng cơ sở."
}

DATA_MOD_10_13[203] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây bạn dùng để xóa một view có tên là EMP_DEPT_VU khỏi schema của bạn?",
    "options_vi": {
        "A": "REMOVE emp_dept_vu;",
        "B": "DELETE emp_dept_vu;",
        "C": "DROP emp_dept_vu",
        "D": "DROP VIEW emp_dept_vu"
    },
    "explanation_vi": "Cú pháp DDL chuẩn để xóa một khung nhìn trong SQL là: `DROP VIEW <tên_view>;`. Lệnh này chỉ xóa định nghĩa của view trong từ điển dữ liệu, hoàn toàn KHÔNG ẢNH HƯỞNG đến dữ liệu của các bảng gốc bên dưới.",
    "key_takeaway_vi": "Xóa View dùng lệnh: DROP VIEW view_name; (không làm mất dữ liệu bảng gốc).",
    "flashcard_front_vi": "Xóa View có làm mất dữ liệu của bảng gốc không?",
    "flashcard_back_vi": "KHÔNG. DROP VIEW chỉ xóa định nghĩa khung nhìn, dữ liệu ở bảng gốc vẫn còn nguyên."
}

DATA_MOD_10_13[204] = {
    "prompt_vi": "Phân tích Top N trong cú pháp truyền thống của Oracle yêu cầu điều gì?",
    "options_vi": {
        "A": "Chỉ cần một inline view.",
        "B": "Sử dụng cột giả ROWNUM (The use of ROWNUM pseudo column).",
        "C": "Sử dụng cột giả ROWID.",
        "D": "Một mệnh đề GROUP BY."
    },
    "explanation_vi": "Trong Oracle truyền thống, để làm Top-N ta dùng một Inline View sắp xếp dữ liệu (`ORDER BY`), sau đó ở câu truy vấn ngoài dùng cột giả `ROWNUM <= N` để giới hạn số dòng lấy ra (ví dụ: `SELECT * FROM (SELECT * FROM emp ORDER BY sal DESC) WHERE ROWNUM <= 3`).",
    "key_takeaway_vi": "Top-N Analysis truyền thống trong Oracle kết hợp Inline View ORDER BY và ROWNUM <= N.",
    "flashcard_front_vi": "Công thức Top-N Analysis truyền thống trong Oracle SQL?",
    "flashcard_back_vi": "SELECT * FROM (SELECT * FROM table ORDER BY col DESC) WHERE ROWNUM <= N;"
}

DATA_MOD_10_13[205] = {
    "prompt_vi": "Điều nào sau đây là ĐÚNG về việc thực hiện cập nhật (update) dữ liệu thông qua một view?",
    "options_vi": {
        "A": "Ràng buộc trên view luôn ghi đè ràng buộc trên bảng gốc.",
        "B": "Khi cập nhật view, các hàm nhóm được tự động tính toán lại.",
        "C": "Bạn KHÔNG THỂ cập nhật một view có chứa các hàm nhóm (cannot update a view with group functions).",
        "D": "Khi cập nhật view, chỉ dữ liệu trong view thay đổi, dữ liệu bảng gốc không đổi."
    },
    "explanation_vi": "Một View phức tạp (Complex View) chứa các hàm nhóm (SUM, AVG...), mệnh đề `GROUP BY`, từ khóa `DISTINCT`, hoặc phép nối nhiều bảng không bảo toàn khóa (key-preserved) thì KHÔNG THỂ thực hiện các thao tác DML (INSERT, UPDATE, DELETE) thông qua View được.",
    "key_takeaway_vi": "Không thể thực hiện DML qua View nếu View chứa hàm nhóm, GROUP BY hoặc DISTINCT.",
    "flashcard_front_vi": "Khi nào một View KHÔNG THỂ cập nhật (update) được?",
    "flashcard_back_vi": "Khi View chứa hàm nhóm (SUM, AVG), mệnh đề GROUP BY, DISTINCT hoặc toán tử SET."
}

DATA_MOD_10_13[206] = {
    "prompt_vi": "Tùy chọn FORCE trong câu lệnh tạo view (CREATE FORCE VIEW) có tác dụng gì?",
    "options_vi": {
        "A": "Tạo view bất kể các bảng cơ sở (base tables) có tồn tại hay không (creates view regardless of whether base tables exist).",
        "B": "Tạo view trong schema khác ngay cả khi không có quyền.",
        "C": "Tạo view ngay cả khi bảng cha có ràng buộc.",
        "D": "Tạo view đi kèm các ràng buộc."
    },
    "explanation_vi": "Mặc định (`NOFORCE`), Oracle chỉ tạo view khi tất cả các bảng cơ sở đã tồn tại và hợp lệ. Khi bạn dùng `CREATE FORCE VIEW`, Oracle sẽ cưỡng chế tạo view ngay cả khi bảng cơ sở chưa tồn tại (hoặc user chưa có quyền), view được tạo ở trạng thái `INVALID` và sẽ tự động biên dịch lại khi bảng được tạo.",
    "key_takeaway_vi": "FORCE cho phép tạo View ngay cả khi bảng cơ sở chưa tồn tại trong cơ sở dữ liệu.",
    "flashcard_front_vi": "Từ khóa FORCE trong CREATE FORCE VIEW dùng để làm gì?",
    "flashcard_back_vi": "Bắt buộc tạo View ngay cả khi bảng gốc chưa được tạo (View sẽ ở trạng thái INVALID)."
}

DATA_MOD_10_13[207] = {
    "prompt_vi": "Điều nào sau đây mô tả đúng nhất về một khung nhìn nội tuyến (inline view)?",
    "options_vi": {
        "A": "Một đối tượng lược đồ (schema object).",
        "B": "Một câu truy vấn con là một phần trong mệnh đề FROM của câu truy vấn khác (subquery in FROM clause).",
        "C": "Một câu truy vấn con có thể chứa mệnh đề ORDER BY.",
        "D": "Tên gọi khác của view có chứa hàm nhóm."
    },
    "explanation_vi": "Inline View là một Subquery được đặt trực tiếp trong mệnh đề `FROM` của câu truy vấn, đóng vai trò như một bảng dữ liệu tạm thời trong phạm vi câu lệnh đó.",
    "key_takeaway_vi": "Inline View = Subquery nằm trong mệnh đề FROM.",
    "flashcard_front_vi": "Inline View nằm ở mệnh đề nào của câu lệnh SELECT?",
    "flashcard_back_vi": "Nằm trong mệnh đề FROM."
}

DATA_MOD_10_13[208] = {
    "prompt_vi": "Phát biểu nào sau đây về các khung nhìn (views) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Một view có thể được tạo ở chế độ chỉ đọc (read only).",
        "B": "Bảng cơ sở bắt buộc phải tồn tại thì mới có thể tạo được view trên nó (The table must exist to create a view on it).",
        "C": "Một view có thể được tạo với mệnh đề GROUP BY trong câu lệnh SELECT.",
        "D": "Một view có thể được tạo dựa trên một view khác."
    },
    "explanation_vi": "Phát biểu B là SAI vì với tùy chọn `CREATE FORCE VIEW`, Oracle hoàn toàn cho phép tạo view ngay cả khi bảng cơ sở CHƯA TỒN TẠI.",
    "key_takeaway_vi": "Bảng cơ sở không nhất thiết phải tồn tại trước nếu dùng tùy chọn CREATE FORCE VIEW.",
    "flashcard_front_vi": "Có bắt buộc bảng phải tồn tại mới tạo được View không?",
    "flashcard_back_vi": "Không bắt buộc nếu sử dụng tùy chọn CREATE FORCE VIEW."
}

DATA_MOD_10_13[209] = {
    "prompt_vi": "Đánh giá câu lệnh SQL sau:\nSELECT a.emp_name, a.sal, a.dept_id, b.maxsal FROM employees a,\n(SELECT dept_id, MAX(sal) maxsal FROM employees GROUP BY dept_id) b\nWHERE a.dept_id = b.dept_id AND a.sal < b.maxsal;\nKết quả của câu lệnh là gì?",
    "options_vi": {
        "A": "Câu lệnh báo lỗi ở dòng 3.",
        "B": "Câu lệnh báo lỗi ở dòng 4.",
        "C": "Trả về tên, lương, mã phòng và lương cao nhất của phòng đó đối với tất cả nhân viên có mức lương THẤP HƠN mức lương cao nhất trong phòng của họ.",
        "D": "Câu lệnh báo lỗi ở dòng 1."
    },
    "explanation_vi": "Khối `b` là một Inline View tính mức lương cao nhất (`maxsal`) của từng phòng ban. Câu lệnh kết nối bảng `employees a` với view `b` theo `dept_id`, và điều kiện `a.sal < b.maxsal` sẽ lọc ra tất cả nhân viên có lương nhỏ hơn người hưởng lương cao nhất phòng.",
    "key_takeaway_vi": "Sử dụng Inline View để so sánh từng dòng dữ liệu của nhân viên với giá trị tổng hợp (MAX) của phòng ban đó.",
    "flashcard_front_vi": "Kỹ thuật dùng Subquery trong FROM ở câu lệnh này giải quyết bài toán gì?",
    "flashcard_back_vi": "So sánh thuộc tính của từng cá nhân với giá trị cực đại (MAX) của nhóm mà cá nhân đó trực thuộc."
}

DATA_MOD_10_13[210] = {
    "prompt_vi": "Bạn cần tạo một view có tên là EMP_VU cho phép người dùng có thể CHÈN (INSERT) các dòng thông qua view. Câu lệnh nào sau đây cho phép chèn dòng?",
    "options_vi": {
        "A": "CREATE VIEW emp_Vu AS SELECT department_id, SUM(sal) TOTALSAL FROM employees WHERE mgr_id IN (102, 120) GROUP BY department_id;",
        "B": "CREATE VIEW emp_Vu AS SELECT employee_id, emp_name,department_id FROM employees WHERE mgr_id IN (102, 120);",
        "C": "CREATE VIEW emp_Vu AS SELECT employee_id, emp_name, job_id,DISTINCT department_id FROM employees;",
        "D": "CREATE VIEW emp_Vu AS SELECT employee_id, emp_name, job_id, department_id FROM employees WHERE mgr_id IN (102, 120); (Theo đáp án CDAC có đủ các cột bắt buộc)"
    },
    "explanation_vi": "Để một View có thể INSERT được dữ liệu vào bảng cơ sở: 1. View không được chứa GROUP BY, DISTINCT hoặc hàm nhóm (loại A và C); 2. View phải chứa TẤT CẢ các cột mang ràng buộc NOT NULL của bảng gốc mà không có giá trị mặc định (câu D chứa đủ các cột bắt buộc của nhân viên).",
    "key_takeaway_vi": "Để View có thể INSERT được: không được có GROUP BY / hàm nhóm, và phải chứa đủ các cột NOT NULL của bảng gốc.",
    "flashcard_front_vi": "Điều kiện để có thể chèn dòng (INSERT) thông qua một View?",
    "flashcard_back_vi": "View đơn giản (không có GROUP BY/hàm nhóm/DISTINCT) và phải chứa tất cả các cột NOT NULL không có DEFAULT."
}

DATA_MOD_10_13[211] = {
    "prompt_vi": "Bạn cần thực hiện các thao tác dữ liệu qua view EMP_DEPT_VU. Bạn muốn xem lại định nghĩa gốc của view (câu lệnh SELECT tạo view). Bạn làm cách nào?",
    "options_vi": {
        "A": "Truy vấn khung nhìn từ điển dữ liệu USER_VIEWS để tìm view EMP_DEPT_VU (Query the USER_VIEWS data dictionary view).",
        "B": "Dùng lệnh DESCRIBE VIEW.",
        "C": "Dùng lệnh DEFINE VIEW.",
        "D": "Truy vấn view USER_SOURCE."
    },
    "explanation_vi": "Trong Oracle, mã lệnh SELECT tạo View được lưu trong cột `TEXT` của từ điển dữ liệu `USER_VIEWS`. Ta chỉ cần truy vấn: `SELECT text FROM user_views WHERE view_name = 'EMP_DEPT_VU';`.",
    "key_takeaway_vi": "Xem câu lệnh SELECT định nghĩa View tra cứu cột TEXT trong view USER_VIEWS.",
    "flashcard_front_vi": "Muốn xem câu lệnh SELECT đã tạo ra một View thì tra cứu ở đâu?",
    "flashcard_back_vi": "Tra cứu view từ điển dữ liệu USER_VIEWS (cột TEXT)."
}

DATA_MOD_10_13[212] = {
    "prompt_vi": "Điều kiện cần thiết để câu truy vấn trên một view hiện có được thực thi thành công là gì?",
    "options_vi": {
        "A": "Các bảng cơ sở phải nằm trong cùng một schema.",
        "B": "Các bảng cơ sở bắt buộc phải có dữ liệu.",
        "C": "Bạn chỉ cần quyền SELECT trên các bảng cơ sở.",
        "D": "Bạn cần có quyền SELECT trên chính khung nhìn đó (You need SELECT privileges on the view)."
    },
    "explanation_vi": "Để truy vấn từ bất kỳ đối tượng nào (bảng hoặc view), người dùng bắt buộc phải được cấp quyền `SELECT` trực tiếp trên đối tượng đó (`GRANT SELECT ON view_name TO user;`). Người dùng không nhất thiết phải có quyền trực tiếp trên các bảng cơ sở bên dưới (đây chính là cơ chế bảo mật phân quyền tuyệt vời của View).",
    "key_takeaway_vi": "Chỉ cần được cấp quyền SELECT trên View là có thể truy vấn View mà không cần quyền trên bảng gốc.",
    "flashcard_front_vi": "Người dùng có cần quyền trên bảng gốc để truy vấn View không?",
    "flashcard_back_vi": "KHÔNG CẦN. Chỉ cần có quyền SELECT trên chính View đó."
}

DATA_MOD_10_13[213] = {
    "prompt_vi": "Khi bạn sử dụng một câu truy vấn con SQL trong mệnh đề ________ của câu lệnh select thì nó được gọi là inline view?",
    "options_vi": {
        "A": "group by",
        "B": "order by",
        "C": "where",
        "D": "from"
    },
    "explanation_vi": "Subquery nằm trong mệnh đề `FROM` được định nghĩa chuẩn là `Inline View`.",
    "key_takeaway_vi": "Subquery trong mệnh đề FROM = Inline View.",
    "flashcard_front_vi": "Subquery nằm trong mệnh đề nào được gọi là Inline View?",
    "flashcard_back_vi": "Mệnh đề FROM."
}

DATA_MOD_10_13[214] = {
    "prompt_vi": "Bạn đã tạo view EMP_DEPT_VU gồm 3 cột. Bây giờ bạn muốn sửa đổi view bằng cách thêm cột thứ tư là MANAGER_ID từ bảng EMPLOYEES. Bạn thực hiện bằng cách nào?",
    "options_vi": {
        "A": "ALTER VIEW emp_dept_vu AS SELECT ...",
        "B": "MODIFY VIEW emp_dept_vu (ADD manager_id NUMBER);",
        "C": "ALTER VIEW emp_dept_vu (ADD manager_id NUMBER);",
        "D": "CREATE OR REPLACE VIEW emp_dept_vu AS SELECT employee_id, employee_name, department_name, manager_id FROM employees e, departments d WHERE e.department_id = d.department_id;"
    },
    "explanation_vi": "Trong Oracle SQL, không có lệnh `ALTER VIEW` để thay đổi định nghĩa cột của view. Để sửa đổi hoặc thêm bớt cột cho view đã có mà không làm mất các quyền (GRANTS) đã cấp trên view, ta sử dụng cú pháp: `CREATE OR REPLACE VIEW <tên_view> AS SELECT ...`.",
    "key_takeaway_vi": "Sửa đổi định nghĩa View dùng: CREATE OR REPLACE VIEW view_name AS ...",
    "flashcard_front_vi": "Làm thế nào để thêm một cột vào View đã tồn tại mà không làm mất phân quyền?",
    "flashcard_back_vi": "Dùng lệnh: CREATE OR REPLACE VIEW tên_view AS SELECT ... (không dùng ALTER VIEW)."
}

DATA_MOD_10_13[215] = {
    "prompt_vi": "Phát biểu nào sau đây về việc tạo một khung nhìn (view) là ĐÚNG?",
    "options_vi": {
        "A": "Các cột trong view là kết quả của giá trị tính toán phái sinh sẽ được Oracle tự đặt tên.",
        "B": "Khi view đã tồn tại, dùng OR REPLACE đòi hỏi phải cấp lại toàn bộ quyền đối tượng đã cấp trước đó.",
        "C": "Tên ràng buộc bắt buộc phải cung cấp khi dùng mệnh đề WITH CHECK OPTION nếu không lệnh sẽ lỗi.",
        "D": "Một view có thể có các tên cột khác với tên cột thực tế của bảng cơ sở bằng cách sử dụng các bí danh cột (by using column aliases)."
    },
    "explanation_vi": "Bạn có thể hoàn toàn đổi tên các cột trong View khác với tên cột của bảng gốc bằng cách sử dụng bí danh cột (`SELECT emp_name AS ho_va_ten ...`) hoặc khai báo danh sách tên cột ngay sau tên view: `CREATE VIEW v_emp (ma_nv, ho_ten) AS SELECT employee_id, emp_name...`.",
    "key_takeaway_vi": "View có thể đặt tên cột khác bảng gốc bằng cách dùng bí danh cột (Column Aliases).",
    "flashcard_front_vi": "Làm thế nào để View có tên cột khác hoàn toàn so với bảng cơ sở?",
    "flashcard_back_vi": "Dùng Column Alias trong câu lệnh SELECT của View hoặc chỉ định danh sách cột sau tên View."
}

DATA_MOD_10_13[216] = {
    "prompt_vi": "Bạn được cấp quyền CREATE VIEW. Quyền này cho phép bạn làm điều gì?",
    "options_vi": {
        "A": "Tạo một table view.",
        "B": "Tạo view trong bất kỳ schema nào.",
        "C": "Tạo một view trong schema của chính bạn (Create a view in your schema).",
        "D": "Tạo sequence view."
    },
    "explanation_vi": "Quyền hệ thống `CREATE VIEW` cho phép người dùng tạo các khung nhìn trong phạm vi schema của chính mình (`in your schema`). Muốn tạo view trong schema của người dùng khác, bạn bắt buộc phải có quyền `CREATE ANY VIEW`.",
    "key_takeaway_vi": "Quyền CREATE VIEW chỉ cho phép tạo view trong chính schema của mình.",
    "flashcard_front_vi": "Quyền CREATE VIEW khác gì với CREATE ANY VIEW?",
    "flashcard_back_vi": "CREATE VIEW chỉ tạo trong schema của mình; CREATE ANY VIEW cho phép tạo trong bất kỳ schema nào."
}

DATA_MOD_10_13[217] = {
    "prompt_vi": "Tùy chọn nào sau đây là một tùy chọn hợp lệ khi tạo một khung nhìn (view)?",
    "options_vi": {
        "A": "WITH BREAK OPTION",
        "B": "ON DELETE CASCADE",
        "C": "WITH GRANT OPTION",
        "D": "WITH CHECK OPTION"
    },
    "explanation_vi": "Khi tạo View, Oracle hỗ trợ hai mệnh đề tùy chọn quan trọng: `WITH READ ONLY` (chỉ cho phép đọc, cấm mọi thao tác DML) và `WITH CHECK OPTION` (chỉ cho phép INSERT/UPDATE nếu bản ghi thỏa mãn điều kiện WHERE của view).",
    "key_takeaway_vi": "Hai tùy chọn phổ biến khi tạo View: WITH CHECK OPTION và WITH READ ONLY.",
    "flashcard_front_vi": "Mệnh đề WITH CHECK OPTION khi tạo View có tác dụng gì?",
    "flashcard_back_vi": "Đảm bảo các thao tác INSERT/UPDATE qua View không thể tạo ra những bản ghi vi phạm điều kiện WHERE của View."
}

DATA_MOD_10_13[218] = {
    "prompt_vi": "Một khung nhìn nội tuyến (inline view) là một câu lệnh SELECT được gán bí danh và được nhúng vào trong mệnh đề ________ của một câu lệnh SELECT khác?",
    "options_vi": {
        "A": "CASE",
        "B": "FROM",
        "C": "WHERE",
        "D": "SELECT"
    },
    "explanation_vi": "Inline view được định nghĩa và nhúng bên trong mệnh đề `FROM` của câu truy vấn ngoài.",
    "key_takeaway_vi": "Inline view nằm trong mệnh đề FROM.",
    "flashcard_front_vi": "Vị trí đặt Inline View trong câu lệnh SELECT?",
    "flashcard_back_vi": "Mệnh đề FROM."
}

DATA_MOD_10_13[219] = {
    "prompt_vi": "Bạn cần tạo view EMP_VU. View này phải cho phép người dùng chỉ được thao tác (INSERT/UPDATE/DELETE) trên các bản ghi của nhân viên thuộc phòng ban 10 hoặc 20. Câu lệnh nào đúng?",
    "options_vi": {
        "A": "CREATE VIEW emp_vu AS SELECT * FROM employees WHERE department_id IN (10,20) WITH READ ONLY;",
        "B": "CREATE VIEW emp_vu AS SELECT * FROM employees WHERE department_id IN (10,20) WITH CHECK OPTION;",
        "C": "CREATE VIEW emp_vu AS SELECT * FROM employees WHERE department_id IN (10,20);",
        "D": "CREATE FORCE VIEW emp_vu AS SELECT * FROM employees WHERE department_id IN (10,20);"
    },
    "explanation_vi": "Mệnh đề `WITH CHECK OPTION` đảm bảo rằng mọi câu lệnh INSERT hoặc UPDATE thông qua view sẽ bị từ chối nếu nó cố gắng thay đổi `department_id` sang một giá trị khác ngoài 10 hoặc 20. Tùy chọn A sai vì `WITH READ ONLY` sẽ cấm hoàn toàn không cho sửa đổi.",
    "key_takeaway_vi": "WITH CHECK OPTION ngăn chặn việc sửa hoặc chèn dữ liệu vi phạm điều kiện WHERE của View.",
    "flashcard_front_vi": "Tại sao dùng WITH CHECK OPTION cho bài toán chỉ cho sửa nhân viên phòng 10, 20?",
    "flashcard_back_vi": "Vì WITH CHECK OPTION sẽ chặn đứng mọi hành vi INSERT/UPDATE nhân viên vào các phòng ban khác ngoài 10 và 20."
}

DATA_MOD_10_13[220] = {
    "prompt_vi": "Phát biểu nào sau đây về các khung nhìn (views) là ĐÚNG?",
    "options_vi": {
        "A": "Một view không thể chứa mệnh đề ORDER BY trong câu lệnh SELECT.",
        "B": "Một view không thể được tạo với mệnh đề GROUP BY.",
        "C": "Một view có thể được tạo ở chế độ chỉ đọc (A view can be created as read only).",
        "D": "Một view bắt buộc phải định nghĩa bí danh cho các cột."
    },
    "explanation_vi": "Bạn hoàn toàn có thể tạo view chỉ đọc bằng cách thêm mệnh đề `WITH READ ONLY` ở cuối câu lệnh `CREATE VIEW`. Khi đó, người dùng chỉ có thể SELECT và không thể INSERT, UPDATE hay DELETE qua view này.",
    "key_takeaway_vi": "Thêm WITH READ ONLY để tạo View chỉ đọc, ngăn chặn mọi thao tác sửa đổi dữ liệu.",
    "flashcard_front_vi": "Làm thế nào để tạo một View chỉ đọc (Read-only) trong Oracle?",
    "flashcard_back_vi": "Thêm mệnh đề WITH READ ONLY vào cuối câu lệnh CREATE VIEW."
}

# MODULE 12: Set Operators and Pseudo Column (Q221 - Q240)
DATA_MOD_10_13[221] = {
    "prompt_vi": "Toán tử nào sau đây KHÔNG PHẢI là một toán tử tập hợp (SET operator) trong SQL?",
    "options_vi": {
        "A": "Intersect",
        "B": "Union",
        "C": "Minus",
        "D": "Plus"
    },
    "explanation_vi": "4 toán tử tập hợp chuẩn trong Oracle SQL là: `UNION`, `UNION ALL`, `INTERSECT`, và `MINUS`. Từ khóa `Plus` là toán tử số học (+), không phải là toán tử tập hợp.",
    "key_takeaway_vi": "4 toán tử tập hợp trong Oracle: UNION, UNION ALL, INTERSECT, MINUS.",
    "flashcard_front_vi": "Kể tên 4 toán tử tập hợp trong Oracle SQL?",
    "flashcard_back_vi": "UNION, UNION ALL, INTERSECT, MINUS."
}

DATA_MOD_10_13[222] = {
    "prompt_vi": "Bảng JOB_HISTORY lưu các nhân viên đã từng đổi công việc ít nhất một lần. Bạn muốn hiển thị mã của những nhân viên CHƯA TỪNG ĐỔI CÔNG VIỆC lần nào. Bạn nên dùng toán tử tập hợp nào?",
    "options_vi": {
        "A": "Intersect",
        "B": "Minus",
        "C": "Union",
        "D": "Union All"
    },
    "explanation_vi": "Bài toán tìm các phần tử thuộc tập A (tất cả nhân viên) nhưng KHÔNG THUỘC tập B (nhân viên đã từng chuyển việc) là phép trừ tập hợp: `SELECT employee_id FROM employees MINUS SELECT employee_id FROM job_history;`. Toán tử `MINUS` thực hiện chính xác phép toán này.",
    "key_takeaway_vi": "Tìm phần tử có trong tập A nhưng không có trong tập B dùng toán tử MINUS.",
    "flashcard_front_vi": "Toán tử MINUS dùng để làm gì trong SQL?",
    "flashcard_back_vi": "Lấy các dòng có trong kết quả truy vấn thứ nhất nhưng KHÔNG CÓ trong kết quả truy vấn thứ hai."
}

DATA_MOD_10_13[223] = {
    "prompt_vi": "Điều nào sau đây là KHÔNG ĐÚNG khi nói về việc sử dụng các toán tử tập hợp (Set operators)?",
    "options_vi": {
        "A": "Các toán tử SET không thể sử dụng trong các câu truy vấn con (SET operators cannot be used in sub queries).",
        "B": "Các biểu thức trong danh sách SELECT phải khớp nhau về số lượng và kiểu dữ liệu tương thích.",
        "C": "Dấu ngoặc đơn có thể được sử dụng để thay đổi thứ tự ưu tiên thực thi.",
        "D": "Các truy vấn sử dụng toán tử tập hợp phải có cùng số lượng và kiểu cột tương ứng."
    },
    "explanation_vi": "Phát biểu A là SAI vì các toán tử tập hợp (UNION, MINUS...) HOÀN TOÀN CÓ THỂ được đặt bên trong các câu truy vấn con (Subqueries).",
    "key_takeaway_vi": "Toán tử tập hợp hoàn toàn có thể được dùng bên trong các câu truy vấn con (Subquery).",
    "flashcard_front_vi": "Có thể dùng toán tử UNION hoặc MINUS bên trong một Subquery không?",
    "flashcard_back_vi": "CÓ. Hoàn toàn hợp lệ khi đặt phép toán tập hợp trong Subquery."
}

DATA_MOD_10_13[224] = {
    "prompt_vi": "Phát biểu nào sau đây về việc sử dụng mệnh đề ORDER BY kết hợp với các toán tử SET là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Tên cột hoặc bí danh cột nếu dùng trong ORDER BY phải lấy từ danh sách SELECT thứ nhất.",
        "B": "Mệnh đề ORDER BY có thể chấp nhận tên cột, bí danh cột hoặc chỉ số vị trí cột (1, 2, 3...).",
        "C": "Mệnh đề ORDER BY chỉ có thể xuất hiện ở điểm cuối cùng của toàn bộ câu lệnh hợp nhất.",
        "D": "Mệnh đề ORDER BY chỉ có thể xuất hiện ở cuối câu lệnh SELECT thứ nhất (Can appear only at the end of the first SELECT)."
    },
    "explanation_vi": "Phát biểu D là SAI. Trong câu lệnh truy vấn ghép nối bằng toán tử SET, mệnh đề `ORDER BY` CHỈ ĐƯỢC PHÉP XUẤT HIỆN DUY NHẤT MỘT LẦN VÀ PHẢI NẰM Ở CUỐI CÙNG của toàn bộ câu lệnh (sau câu SELECT cuối cùng). Đặt ORDER BY ở câu SELECT đầu tiên sẽ gây lỗi cú pháp.",
    "key_takeaway_vi": "ORDER BY trong truy vấn tập hợp chỉ được đặt ở cuối cùng của toàn bộ câu lệnh.",
    "flashcard_front_vi": "Vị trí đặt mệnh đề ORDER BY khi kết hợp nhiều câu lệnh SELECT bằng UNION/MINUS?",
    "flashcard_back_vi": "Chỉ được đặt duy nhất 1 lần ở cuối cùng của toàn bộ câu lệnh truy vấn ghép."
}

DATA_MOD_10_13[225] = {
    "prompt_vi": "Phát biểu nào sau đây về Oracle Server và các toán tử SET là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Theo mặc định, kết quả đầu ra được sắp xếp tăng dần theo cột đầu tiên của mệnh đề SELECT.",
        "B": "Tên các cột trong kết quả đầu ra được quyết định bởi danh sách cột của câu lệnh SELECT đầu tiên.",
        "C": "Kiểu dữ liệu của các cột đầu ra giống hệt như các cột được chọn (Theo đáp án trắc nghiệm đề CDAC đánh dấu 100)",
        "D": "Oracle Server tự động loại bỏ các dòng trùng lặp, ngoại trừ trường hợp dùng toán tử UNION ALL."
    },
    "explanation_vi": "Các toán tử UNION, INTERSECT, MINUS tự động sắp xếp kết quả tăng dần và loại bỏ bản ghi trùng lặp. Tên cột hiển thị ở kết quả luôn lấy theo câu SELECT đầu tiên. Kiểu dữ liệu của các cột tương ứng chỉ cần thuộc cùng nhóm kiểu tương thích (Oracle sẽ tự chuyển đổi kiểu ngầm định chứ không bắt buộc phải giống hệt tuyệt đối).",
    "key_takeaway_vi": "Tên tiêu đề cột đầu ra trong phép toán SET luôn lấy theo câu SELECT đầu tiên.",
    "flashcard_front_vi": "Tên cột kết quả trong truy vấn UNION lấy theo câu lệnh SELECT nào?",
    "flashcard_back_vi": "Luôn lấy theo tên cột (hoặc bí danh) của câu lệnh SELECT ĐẦU TIÊN."
}

DATA_MOD_10_13[226] = {
    "prompt_vi": "Bảng DUAL trong Oracle mặc định chứa dữ liệu gì?",
    "options_vi": {
        "A": "Một cột có tên là DUMMY và một dòng duy nhất mang giá trị 'X' (One column named DUMMY and one row with value X).",
        "B": "Một cột có tên là D và một dòng có giá trị X.",
        "C": "Một cột có tên là COL và một dòng có giá trị 1.",
        "D": "Bảng DUAL mặc định không chứa bất kỳ dữ liệu nào."
    },
    "explanation_vi": "Bảng `DUAL` là bảng đặc biệt thuộc schema SYS trong Oracle, dùng để tính toán biểu thức hoặc gọi hàm đơn dòng. Cấu trúc của bảng DUAL chỉ gồm duy nhất 1 cột mang tên `DUMMY VARCHAR2(1)` và chứa duy nhất 1 dòng có giá trị là chữ cái `'X'`.",
    "key_takeaway_vi": "Bảng DUAL gồm 1 cột DUMMY và 1 dòng duy nhất có giá trị 'X'.",
    "flashcard_front_vi": "Bảng DUAL trong Oracle có cấu trúc và dữ liệu như thế nào?",
    "flashcard_back_vi": "Gồm 1 cột tên DUMMY (VARCHAR2(1)) và 1 dòng duy nhất chứa giá trị 'X'."
}

DATA_MOD_10_13[227] = {
    "prompt_vi": "Điều nào sau đây KHÔNG ĐÚNG khi nói về các cột giả (Pseudo columns) trong Oracle?",
    "options_vi": {
        "A": "Một cột giả hoạt động giống như một cột của bảng nhưng không thực sự được lưu trữ trong bảng.",
        "B": "Các cột giả được quản lý và duy trì nội bộ bởi Oracle Server.",
        "C": "Bạn không thể chèn giá trị của một cột giả vào cột của bảng khác (You cannot insert value of a pseudo column).",
        "D": "Bạn có thể SELECT từ các cột giả nhưng không thể INSERT, UPDATE hoặc DELETE trực tiếp giá trị của chính nó."
    },
    "explanation_vi": "Phát biểu C là SAI hoàn toàn. Bạn HOÀN TOÀN CÓ THỂ lấy giá trị của cột giả (như `sequence.NEXTVAL`, `ROWNUM`, `SYSDATE`) để INSERT hoặc UPDATE vào các cột thực tế của một bảng: `INSERT INTO orders (id) VALUES (order_seq.NEXTVAL);`.",
    "key_takeaway_vi": "Giá trị của cột giả (như sequence.NEXTVAL) hoàn toàn có thể được INSERT vào bảng khác.",
    "flashcard_front_vi": "Có thể dùng giá trị của cột giả (như sequence.NEXTVAL) để INSERT vào bảng không?",
    "flashcard_back_vi": "CÓ. Hoàn toàn được phép dùng giá trị cột giả để chèn hoặc cập nhật vào bảng."
}

DATA_MOD_10_13[228] = {
    "prompt_vi": "Tên nào sau đây KHÔNG PHẢI là một loại hoặc tên cột giả (Pseudo-column) hợp lệ trong Oracle?",
    "options_vi": {
        "A": "Hierarchical Query Pseudo columns (LEVEL)",
        "B": "Sequence Pseudo columns (NEXTVAL, CURRVAL)",
        "C": "Sub Query Pseudo columns (Cột giả truy vấn con)",
        "D": "ROWNUM Pseudo column"
    },
    "explanation_vi": "Trong Oracle có các nhóm cột giả: Phân cấp (LEVEL), Sequence (NEXTVAL, CURRVAL), Vị trí/Số thứ tự dòng (ROWNUM, ROWID). Không có nhóm nào tên là 'Sub Query Pseudo columns'.",
    "key_takeaway_vi": "Không có loại cột giả nào tên là Sub Query Pseudo columns.",
    "flashcard_front_vi": "Kể tên các cột giả (Pseudocolumns) phổ biến trong Oracle?",
    "flashcard_back_vi": "ROWNUM, ROWID, LEVEL, NEXTVAL, CURRVAL."
}

DATA_MOD_10_13[229] = {
    "prompt_vi": "Phát biểu nào sau đây về các cột giả của chuỗi Sequence (NEXTVAL, CURRVAL) là ĐÚNG?",
    "options_vi": {
        "A": "Bạn dùng CURRVAL để sinh giá trị mới từ sequence.",
        "B": "Bạn dùng NEXTVAL để xem trước giá trị tiếp theo mà không thực sự lấy giá trị đó.",
        "C": "Bạn dùng CURRVAL để sinh giá trị tiếp theo cần dùng.",
        "D": "Bạn dùng NEXTVAL để lấy giá trị khả dĩ tiếp theo từ sequence bằng cách thực sự trích xuất giá trị đó (by actually retrieving the value)."
    },
    "explanation_vi": "`NEXTVAL` trích xuất giá trị tiếp theo của sequence và làm tăng sequence lên một bước nhảy. `CURRVAL` chỉ dùng để tham chiếu lại giá trị vừa được sinh ra bởi NEXTVAL trong phiên hiện tại (không thể gọi CURRVAL trước khi gọi NEXTVAL).",
    "key_takeaway_vi": "NEXTVAL sinh ra và trích xuất giá trị mới của Sequence; CURRVAL trả về giá trị hiện tại vừa sinh.",
    "flashcard_front_vi": "Phân biệt NEXTVAL và CURRVAL của Sequence?",
    "flashcard_back_vi": "NEXTVAL tăng sequence và sinh giá trị mới. CURRVAL đọc lại giá trị hiện tại vừa được sinh bởi NEXTVAL."
}

DATA_MOD_10_13[230] = {
    "prompt_vi": "Thông tin nào sau đây KHÔNG NẰM TRONG thông tin được mã hóa bên trong cột giả ROWID?",
    "options_vi": {
        "A": "Mã số đối tượng dữ liệu (data object number).",
        "B": "Tệp dữ liệu (datafile) chứa dòng đó.",
        "C": "Vị trí của dòng trong bảng Oracle (The position of the row in the oracle table).",
        "D": "Khối dữ liệu (data block) trong datafile chứa dòng đó."
    },
    "explanation_vi": "Cấu trúc một `ROWID mở rộng (Extended ROWID)` gồm 18 ký tự mã hóa 4 thành phần: 1. Data Object Number (6 ký tự); 2. Datafile Relative Number (3 ký tự); 3. Data Block Number (6 ký tự); 4. Row Number bên trong khối dữ liệu (3 ký tự). Nó không lưu 'vị trí tuyệt đối của dòng trong bảng' (vì trong mô hình quan hệ bảng không có thứ tự dòng cố định).",
    "key_takeaway_vi": "ROWID chứa: Object ID, Datafile ID, Block ID, Row Slot trong Block. Không chứa thứ tự dòng trong bảng.",
    "flashcard_front_vi": "ROWID trong Oracle chứa những thành phần cấu trúc vật lý nào?",
    "flashcard_back_vi": "Data Object ID, Relative Datafile ID, Block ID và Row number bên trong Block."
}

DATA_MOD_10_13[231] = {
    "prompt_vi": "Cột giả nào sau đây hữu ích khi thực hiện phân tích TOP-N trong Oracle?",
    "options_vi": {
        "A": "RANK",
        "B": "ROWID",
        "C": "LEVEL",
        "D": "ROWNUM"
    },
    "explanation_vi": "Cột giả `ROWNUM` đánh số thứ tự tuần tự cho các dòng kết quả trả về từ 1. Khi kết hợp với Inline View sắp xếp ORDER BY, `ROWNUM <= N` là kỹ thuật chuẩn để lấy ra Top N bản ghi.",
    "key_takeaway_vi": "Top-N Analysis trong Oracle truyền thống sử dụng cột giả ROWNUM.",
    "flashcard_front_vi": "Cột giả nào dùng để giới hạn số dòng (Top-N) trong Oracle SQL?",
    "flashcard_back_vi": "ROWNUM (kết hợp WHERE ROWNUM <= N)."
}

DATA_MOD_10_13[232] = {
    "prompt_vi": "Bạn muốn lấy chi tiết nhân viên từ 2 bảng khác nhau có thể chứa các mã nhân viên trùng nhau, nhưng muốn hiển thị mỗi bản ghi nhân viên DUY NHẤT MỘT LẦN (loại bỏ trùng). Bạn nên dùng toán tử SET nào?",
    "options_vi": {
        "A": "Union",
        "B": "Union all",
        "C": "Minus",
        "D": "Intersect"
    },
    "explanation_vi": "Toán tử `UNION` gộp kết quả của 2 truy vấn và TỰ ĐỘNG LOẠI BỎ CÁC DÒNG TRÙNG LẶP (Duplicate elimination). Ngược lại, `UNION ALL` giữ lại toàn bộ các dòng trùng lặp.",
    "key_takeaway_vi": "Gộp dữ liệu và loại bỏ trùng lặp dùng UNION; giữ nguyên trùng lặp dùng UNION ALL.",
    "flashcard_front_vi": "Phân biệt UNION và UNION ALL?",
    "flashcard_back_vi": "UNION tự động loại bỏ các dòng trùng lặp và sắp xếp kết quả; UNION ALL giữ nguyên tất cả dòng trùng lặp."
}

DATA_MOD_10_13[233] = {
    "prompt_vi": "Kết quả xuất ra của câu lệnh sau là gì?\nSELECT * FROM employees WHERE ROWNUM < 10;",
    "options_vi": {
        "A": "Thực hiện phân tích TOP-N để hiển thị 9 nhân viên có thu nhập cao nhất.",
        "B": "Báo lỗi vì ROWNUM không nằm trong mệnh đề SELECT.",
        "C": "Chỉ chọn đúng 10 bản ghi từ bảng employees.",
        "D": "Trả về 9 dòng từ bảng Employees (nếu bảng có từ 9 bản ghi trở lên)."
    },
    "explanation_vi": "Điều kiện `ROWNUM < 10` giới hạn các dòng có số thứ tự ROWNUM từ 1 đến 9. Do đó câu lệnh sẽ trả về chính xác 9 dòng dữ liệu đầu tiên được quét từ bảng.",
    "key_takeaway_vi": "WHERE ROWNUM < 10 trả về đúng 9 bản ghi (từ 1 đến 9).",
    "flashcard_front_vi": "Điều kiện WHERE ROWNUM < 10 trả về bao nhiêu dòng?",
    "flashcard_back_vi": "Trả về 9 dòng (ROWNUM = 1, 2, ..., 9)."
}

DATA_MOD_10_13[234] = {
    "prompt_vi": "Các câu truy vấn có chứa các toán tử SET được gọi là các câu truy vấn ________?",
    "options_vi": {
        "A": "Hợp chất / Phức hợp (Compound queries)",
        "B": "Set queries",
        "C": "Complex queries",
        "D": "Set Manipulation queries"
    },
    "explanation_vi": "Trong tài liệu chuẩn của Oracle Database, một câu lệnh SQL kết hợp kết quả của hai hoặc nhiều câu lệnh SELECT bằng các toán tử tập hợp (UNION, UNION ALL, INTERSECT, MINUS) được định nghĩa chính thức là một `Compound Query` (Truy vấn phức hợp).",
    "key_takeaway_vi": "Truy vấn dùng toán tử tập hợp gọi là Compound Query.",
    "flashcard_front_vi": "Tên gọi chính thức của câu truy vấn chứa toán tử SET là gì?",
    "flashcard_back_vi": "Compound Query (Truy vấn phức hợp)."
}

DATA_MOD_10_13[235] = {
    "prompt_vi": "Điều nào sau đây là KHÔNG ĐÚNG khi nói về toán tử Union?",
    "options_vi": {
        "A": "UNION hoạt động trên toàn bộ tất cả các cột được chọn trong SELECT.",
        "B": "Toán tử IN có độ ưu tiên cao hơn toán tử UNION.",
        "C": "Mặc định, kết quả đầu ra được sắp xếp tăng dần theo cột đầu tiên của SELECT.",
        "D": "Các giá trị NULL bị bỏ qua trong quá trình kiểm tra trùng lặp (NULL values are ignored during duplicate checking)."
    },
    "explanation_vi": "Phát biểu D là SAI vì toán tử `UNION` KHÔNG BỎ QUA giá trị NULL khi so khớp trùng lặp. Nếu cả hai câu truy vấn đều trả về một dòng có giá trị NULL giống nhau, UNION sẽ xem chúng là trùng lặp và chỉ giữ lại một giá trị NULL duy nhất.",
    "key_takeaway_vi": "UNION không bỏ qua NULL khi lọc trùng lặp; hai giá trị NULL được coi là trùng lặp và gộp thành 1.",
    "flashcard_front_vi": "Toán tử UNION xử lý các dòng có giá trị NULL trùng nhau như thế nào?",
    "flashcard_back_vi": "Nó coi các giá trị NULL trùng nhau là dữ liệu trùng lặp và chỉ giữ lại 1 dòng duy nhất."
}

DATA_MOD_10_13[236] = {
    "prompt_vi": "Toán tử tập hợp nào sau đây khi sử dụng thì kết quả trả về KHÔNG ĐƯỢC tự động sắp xếp theo mặc định?",
    "options_vi": {
        "A": "Minus",
        "B": "Intersect",
        "C": "Union",
        "D": "Union All"
    },
    "explanation_vi": "Các toán tử `UNION`, `INTERSECT`, `MINUS` đều cần loại bỏ dòng trùng lặp nên Oracle tự động thực hiện thao tác Sort Unique (sắp xếp tăng dần). Riêng `UNION ALL` chỉ đơn thuần ghép nối các tập dữ liệu lại với nhau mà không lọc trùng, do đó nó KHÔNG thực hiện sắp xếp.",
    "key_takeaway_vi": "UNION ALL là toán tử SET duy nhất không tự động sắp xếp kết quả.",
    "flashcard_front_vi": "Tại sao UNION ALL có hiệu năng cao hơn UNION?",
    "flashcard_back_vi": "Vì UNION ALL không mất chi phí sắp xếp (sort) và không phải quét tìm dòng trùng lặp."
}

DATA_MOD_10_13[237] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về toán tử UNION ALL?",
    "options_vi": {
        "A": "Từ khóa DISTINCT có thể được sử dụng (The DISTINCT keyword can be used).",
        "B": "Kết quả đầu ra không được sắp xếp theo mặc định.",
        "C": "Toán tử UNION ALL trả về tất cả các dòng từ nhiều câu truy vấn.",
        "D": "Các dòng trùng lặp không bị loại bỏ."
    },
    "explanation_vi": "Bản thân `UNION ALL` sinh ra là để lấy tất cả các dòng kể cả trùng lặp. Cú pháp `UNION ALL DISTINCT` không tồn tại trong SQL (nếu muốn loại trùng thì đã dùng toán tử `UNION`). Do đó phương án A là phát biểu SAI.",
    "key_takeaway_vi": "UNION ALL không đi kèm với từ khóa DISTINCT.",
    "flashcard_front_vi": "Có cú pháp UNION ALL DISTINCT trong SQL không?",
    "flashcard_back_vi": "KHÔNG. Muốn loại bỏ trùng lặp chỉ dùng từ khóa UNION."
}

DATA_MOD_10_13[238] = {
    "prompt_vi": "Điều nào sau đây là KHÔNG ĐÚNG khi nói về việc sử dụng toán tử Intersect?",
    "options_vi": {
        "A": "INTERSECT không bỏ qua các giá trị NULL.",
        "B": "Tên của các cột không bắt buộc phải giống hệt nhau giữa các câu SELECT.",
        "C": "Số lượng cột và kiểu dữ liệu của các cột được chọn phải tương thích trong tất cả các câu SELECT.",
        "D": "Đảo ngược thứ tự các bảng trong phép giao có thể làm thay đổi kết quả đầu ra (Reversing order may result in changed output)."
    },
    "explanation_vi": "Phát biểu D là SAI vì phép giao tập hợp có tính chất giao hoán: `A INTERSECT B` luôn luôn cho ra kết quả giống hệt như `B INTERSECT A`. Việc đảo thứ tự không làm thay đổi tập dữ liệu trả về (chỉ có phép trừ `MINUS` mới không giao hoán: `A - B != B - A`).",
    "key_takeaway_vi": "Phép INTERSECT có tính giao hoán: A INTERSECT B = B INTERSECT A.",
    "flashcard_front_vi": "Đảo vị trí giữa 2 câu SELECT trong phép INTERSECT có làm đổi kết quả không?",
    "flashcard_back_vi": "KHÔNG. Phép giao có tính chất giao hoán (khác với phép trừ MINUS)."
}

DATA_MOD_10_13[239] = {
    "prompt_vi": "Bạn nên sử dụng toán tử nào để hiển thị các bản ghi là kết quả chung (giao nhau) của cả hai câu truy vấn?",
    "options_vi": {
        "A": "Union",
        "B": "Minus",
        "C": "Intersect",
        "D": "Union All"
    },
    "explanation_vi": "Toán tử `INTERSECT` (phép giao) trả về các dòng xuất hiện đồng thời trong cả hai tập kết quả của câu truy vấn thứ nhất và câu truy vấn thứ hai.",
    "key_takeaway_vi": "Tìm các dòng chung giữa 2 tập kết quả dùng toán tử INTERSECT.",
    "flashcard_front_vi": "Toán tử tập hợp nào tìm phần tử chung của 2 truy vấn?",
    "flashcard_back_vi": "INTERSECT."
}

DATA_MOD_10_13[240] = {
    "prompt_vi": "Điều nào sau đây là ĐÚNG về việc sử dụng toán tử Union?",
    "options_vi": {
        "A": "Kiểu dữ liệu phải giống nhau nhưng số lượng cột có thể khác nhau.",
        "B": "Số lượng cột và kiểu dữ liệu của các cột được chọn phải tương thích ở tất cả các câu lệnh SELECT (number and data types must be identical).",
        "C": "Tên của các cột cũng bắt buộc phải giống nhau hoàn toàn.",
        "D": "Số lượng cột phải bằng nhau nhưng kiểu dữ liệu có thể khác nhau."
    },
    "explanation_vi": "Quy tắc bắt buộc của mọi toán tử tập hợp (UNION, INTERSECT, MINUS): 1. Số lượng cột ở các mệnh đề SELECT phải BẰNG NHAU; 2. Kiểu dữ liệu của các cột ở từng vị trí tương ứng phải THUỘC CÙNG NHÓM KIỂU TƯƠNG THÍCH. Tên cột không bắt buộc phải giống nhau.",
    "key_takeaway_vi": "Phép toán tập hợp bắt buộc số lượng cột và kiểu dữ liệu tương ứng phải khớp nhau.",
    "flashcard_front_vi": "Quy tắc về cột khi kết hợp 2 câu SELECT bằng toán tử SET?",
    "flashcard_back_vi": "Cùng số lượng cột và các cột tương ứng cùng thứ tự phải tương thích kiểu dữ liệu."
}

# MODULE 13: Normalization (Q241 - Q260)
DATA_MOD_10_13[241] = {
    "prompt_vi": "Phát biểu nào sau đây KHÔNG ĐÚNG khi nói về Chuẩn hóa cơ sở dữ liệu (Database Normalization)?",
    "options_vi": {
        "A": "Chuẩn hóa thường bao gồm việc gộp các bảng nhỏ lại thành một bảng duy nhất để truy cập tối đa dữ liệu qua mỗi bảng (combining small tables into a single table).",
        "B": "Trong thiết kế RDBMS, quá trình tổ chức dữ liệu để giảm thiểu sự dư thừa được gọi là 'Chuẩn hóa'.",
        "C": "Mục tiêu của chuẩn hóa là phân rã các quan hệ có dị thường để tạo ra các quan hệ nhỏ hơn, có cấu trúc tốt.",
        "D": "Chuẩn hóa thường bao gồm việc chia tách các bảng lớn thành các bảng nhỏ hơn và thiết lập mối quan hệ giữa chúng."
    },
    "explanation_vi": "Phát biểu A là SAI hoàn toàn vì bản chất của chuẩn hóa là PHÂN RÃ (Decomposition): chia tách các bảng lớn chứa dữ liệu dư thừa và dị thường thành các bảng nhỏ hơn chuyên biệt, chứ không phải gộp các bảng nhỏ lại thành một bảng to (đó là Denormalization - phi chuẩn hóa).",
    "key_takeaway_vi": "Chuẩn hóa là phân rã bảng lớn thành các bảng nhỏ hơn để loại bỏ dư thừa và dị thường dữ liệu.",
    "flashcard_front_vi": "Bản chất của chuẩn hóa CSDL (Normalization) là gì?",
    "flashcard_back_vi": "Phân rã bảng lớn thành các bảng nhỏ hơn để loại bỏ dư thừa và ngăn chặn dị thường."
}

DATA_MOD_10_13[242] = {
    "prompt_vi": "Một thuộc tính được gọi là phụ thuộc hàm đầy đủ (fully functionally dependent) vào tập thuộc tính X nếu nó:",
    "options_vi": {
        "A": "Phụ thuộc hàm vào X (Functionally dependent on X).",
        "B": "Không phụ thuộc hàm vào bất kỳ tập con thực sự nào của X (Not functionally dependent on any proper subset of X).",
        "C": "Hoặc A hoặc B nhưng không phải cả hai.",
        "D": "Thỏa mãn cả A và B (Both A and B)."
    },
    "explanation_vi": "Định nghĩa lý thuyết: Thuộc tính Y phụ thuộc hàm đầy đủ vào khóa tổng hợp X khi và chỉ khi: 1. Y phụ thuộc vào toàn bộ X; VÀ 2. Y không phụ thuộc vào bất kỳ phần nào (tập con thực sự) của X. Nếu Y chỉ phụ thuộc vào một phần của X thì đó là Phụ thuộc hàm một phần (Partial Dependency).",
    "key_takeaway_vi": "Phụ thuộc hàm đầy đủ = Phụ thuộc vào toàn bộ khóa X và không phụ thuộc vào bất kỳ tập con nào của X.",
    "flashcard_front_vi": "Thế nào là Phụ thuộc hàm đầy đủ (Full Functional Dependency)?",
    "flashcard_back_vi": "Y phụ thuộc vào toàn bộ tập thuộc tính khóa X và không phụ thuộc vào bất kỳ tập con thực sự nào của X."
}

DATA_MOD_10_13[243] = {
    "prompt_vi": "Điều nào sau đây là ĐÚNG khi nói về Phụ thuộc đa trị (Multivalued dependency)?",
    "options_vi": {
        "A": "Phụ thuộc đa trị là ràng buộc mà sự hiện diện của khóa chính ngụ ý sự hiện diện của khóa ngoại.",
        "B": "Phụ thuộc đa trị là ràng buộc mà sự hiện diện của một số dòng nhất định trong bảng ngụ ý sự hiện diện của một số dòng khác (presence of certain rows implies presence of other rows).",
        "C": "Phụ thuộc hàm ngụ ý phụ thuộc bắc cầu.",
        "D": "Phụ thuộc bắc cầu ngụ ý phụ thuộc hàm."
    },
    "explanation_vi": "Định nghĩa của Phụ thuộc đa trị (Multivalued Dependency: `X ->> Y`): Với các giá trị đã cho của X, tập các giá trị của Y hoàn toàn độc lập với các thuộc tính còn lại Z. Do đó, nếu bảng có các dòng `(x, y1, z2)` và `(x, y2, z1)` thì bắt buộc phải có mặt cả các dòng `(x, y1, z1)` và `(x, y2, z2)`. Đây là nền tảng của dạng chuẩn 4NF.",
    "key_takeaway_vi": "Phụ thuộc đa trị (X ->> Y) quy định sự tồn tại của cặp dòng này suy ra sự hiện diện của cặp dòng khác.",
    "flashcard_front_vi": "Phụ thuộc đa trị (Multivalued Dependency) liên quan đến dạng chuẩn nào?",
    "flashcard_back_vi": "Dạng chuẩn 4NF (loại bỏ phụ thuộc đa trị không tầm thường)."
}

DATA_MOD_10_13[244] = {
    "prompt_vi": "Phát biểu nào sau đây là ĐÚNG khi nói về Siêu khóa (Super Keys)?",
    "options_vi": {
        "A": "Một siêu khóa không thể là một khóa ứng viên.",
        "B": "Một bảng chỉ có thể có duy nhất một siêu khóa.",
        "C": "Siêu khóa có thể không chứa tất cả các cột có trong khóa ứng viên.",
        "D": "Một siêu khóa là một tập hợp các thuộc tính có thể dùng để định danh duy nhất một bản ghi trong bảng (uniquely identify a record)."
    },
    "explanation_vi": "Định nghĩa: `Siêu khóa (Super Key)` là bất kỳ tập hợp một hoặc nhiều thuộc tính nào mà giá trị của chúng có thể phân biệt duy nhất từng dòng trong bảng. Khóa ứng viên (Candidate Key) là một siêu khóa tối thiểu (minimal super key).",
    "key_takeaway_vi": "Siêu khóa là tập thuộc tính xác định duy nhất một bản ghi trong bảng quan hệ.",
    "flashcard_front_vi": "Mối quan hệ giữa Siêu khóa (Super Key) và Khóa ứng viên (Candidate Key)?",
    "flashcard_back_vi": "Mọi Khóa ứng viên đều là Siêu khóa, và là Siêu khóa tối thiểu (không thể bỏ bớt thuộc tính nào)."
}

DATA_MOD_10_13[245] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Một thuộc tính khóa (prime attribute) cũng là một phần của tất cả các siêu khóa chứa nó.",
        "B": "Một thuộc tính khóa (prime attribute) là thuộc tính xuất hiện trong bất kỳ khóa ứng viên nào.",
        "C": "Một thuộc tính không khóa là thuộc tính không xuất hiện trong bất kỳ siêu khóa nào (does not occur in any super key).",
        "D": "Một thuộc tính không khóa (non-prime attribute) là thuộc tính không xuất hiện trong bất kỳ khóa ứng viên nào."
    },
    "explanation_vi": "Phát biểu C là SAI vì một thuộc tính không khóa (Non-prime attribute) hoàn toàn có thể tham gia vào một siêu khóa (bởi vì siêu khóa là khóa ứng viên cộng thêm các thuộc tính bất kỳ khác, bao gồm cả thuộc tính không khóa). Định nghĩa chuẩn: Thuộc tính không khóa là thuộc tính không tham gia vào BẤT KỲ KHÓA ỨNG VIÊN nào.",
    "key_takeaway_vi": "Thuộc tính không khóa (Non-prime) là thuộc tính không nằm trong bất kỳ Khóa ứng viên (Candidate Key) nào.",
    "flashcard_front_vi": "Định nghĩa thuộc tính khóa (Prime) và không khóa (Non-prime)?",
    "flashcard_back_vi": "Prime attribute thuộc ít nhất một Candidate Key; Non-prime attribute không thuộc bất kỳ Candidate Key nào."
}

DATA_MOD_10_13[246] = {
    "prompt_vi": "Điều kiện nào sau đây KHÔNG PHẢI là một điều kiện hợp lệ để một bảng đạt Dạng chuẩn 1 (1NF)?",
    "options_vi": {
        "A": "Không có các dòng trùng lặp.",
        "B": "Không có thứ tự từ trên xuống dưới đối với các dòng.",
        "C": "Có thứ tự từ trái qua phải đối với các cột (There's left-to-right ordering to the columns).",
        "D": "Mỗi giao điểm giữa dòng và cột chỉ chứa duy nhất một giá trị nguyên tử (atomic value) thuộc miền áp dụng."
    },
    "explanation_vi": "Trong lý thuyết cơ sở dữ liệu quan hệ của E.F. Codd: Thứ tự các cột (từ trái qua phải) và thứ tự các dòng (từ trên xuống dưới) là hoàn toàn KHÔNG CÓ Ý NGHĨA. Việc yêu cầu 'phải có thứ tự từ trái qua phải đối với các cột' là phát biểu SAI.",
    "key_takeaway_vi": "Trong bảng quan hệ chuẩn 1NF, thứ tự cột và thứ tự dòng không có ý nghĩa.",
    "flashcard_front_vi": "Điều kiện cốt lõi của Dạng chuẩn 1 (1NF) là gì?",
    "flashcard_back_vi": "Mọi giá trị thuộc tính phải là nguyên tử (Atomic values - đơn trị), không có nhóm lặp."
}

DATA_MOD_10_13[247] = {
    "prompt_vi": "Xét bảng Employees' Skills (Employee, Skill, Current Work Location).\nJones có 3 kỹ năng khác nhau nhưng đều ở địa chỉ '114 Main Street'. Tại sao bảng 1NF này CHƯA ĐẠT dạng chuẩn 2 (2NF)?",
    "options_vi": {
        "A": "Các thuộc tính không khóa không phụ thuộc vào toàn bộ các thuộc tính khóa (phụ thuộc một phần).",
        "B": "Bảng chứa nhiều bản ghi cho cùng một tên nhân viên.",
        "C": "Các thuộc tính không khóa phụ thuộc vào từng thuộc tính khóa.",
        "D": "Bảng chưa đạt 1NF."
    },
    "explanation_vi": "Khóa chính của bảng là khóa tổng hợp `(Employee, Skill)`. Thuộc tính không khóa `Current Work Location` (địa điểm làm việc) chỉ phụ thuộc vào `Employee` chứ không phụ thuộc vào `Skill` (Jones làm ở đâu thì mọi kỹ năng của anh ta đều ở địa chỉ đó). Đây là `Phụ thuộc hàm một phần (Partial Dependency)`, vi phạm quy tắc của Dạng chuẩn 2 (2NF).",
    "key_takeaway_vi": "Bảng vi phạm 2NF khi thuộc tính không khóa chỉ phụ thuộc vào một phần của khóa chính tổng hợp.",
    "flashcard_front_vi": "Điều kiện để một quan hệ đạt Dạng chuẩn 2 (2NF)?",
    "flashcard_back_vi": "Đã ở 1NF và KHÔNG CÒN phụ thuộc hàm một phần (mọi thuộc tính không khóa phải phụ thuộc đầy đủ vào khóa chính)."
}

DATA_MOD_10_13[248] = {
    "prompt_vi": "Xét bảng Tournament Winners (Tournament, Year, Winner, Winner Date of Birth).\nĐiều kiện nào của Dạng chuẩn 3 (3NF) bị bảng dưới đây vi phạm?",
    "options_vi": {
        "A": "Mọi thuộc tính khóa của bảng phải phụ thuộc không bắc cầu.",
        "B": "Mọi thuộc tính không khóa phải phụ thuộc không bắc cầu vào mọi khóa ứng viên (non-transitively dependent).",
        "C": "Bảng phải đạt 2NF.",
        "D": "Bảng phải đạt 1NF."
    },
    "explanation_vi": "Khóa chính của giải đấu là `(Tournament, Year)`. Khóa chính xác định `Winner` (người chiến thắng). Sau đó `Winner` lại xác định `Winner Date of Birth` (ngày sinh của người chiến thắng). Tức là: `(Tournament, Year) -> Winner -> Winner Date of Birth`. Đây là `Phụ thuộc hàm bắc cầu (Transitive Dependency)`, vi phạm trực tiếp quy tắc của Dạng chuẩn 3 (3NF).",
    "key_takeaway_vi": "3NF loại bỏ phụ thuộc bắc cầu: Thuộc tính không khóa không được phụ thuộc vào thuộc tính không khóa khác.",
    "flashcard_front_vi": "Điều kiện để đạt Dạng chuẩn 3 (3NF) là gì?",
    "flashcard_back_vi": "Đã đạt 2NF và KHÔNG CÓ phụ thuộc hàm bắc cầu giữa các thuộc tính không khóa."
}

DATA_MOD_10_13[249] = {
    "prompt_vi": "Phát biểu nào sau đây về Dạng chuẩn Boyce-Codd (BCNF) là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Chỉ trong một số trường hợp hiếm hoi thì bảng 3NF mới không đáp ứng yêu cầu của BCNF.",
        "B": "BCNF được phát triển để giải quyết một số dạng dị thường mà định nghĩa ban đầu của 3NF chưa xử lý được.",
        "C": "Dạng chuẩn Boyce-Codd là một phiên bản mạnh hơn một chút so với dạng chuẩn 3.",
        "D": "Một bảng 3NF không có nhiều khóa ứng viên chồng chéo được cho là không đạt BCNF (Theo đáp án CDAC đánh dấu 100)"
    },
    "explanation_vi": "Định lý chuẩn hóa: Nếu một bảng đạt 3NF và KHÔNG CÓ các khóa ứng viên gối nhau/chồng chéo (overlapping candidate keys), thì bảng đó CHẮC CHẮN ĐÃ ĐẠT BCNF! Do đó phát biểu D nói rằng bảng như vậy 'không đạt BCNF' là phát biểu SAI.",
    "key_takeaway_vi": "Một bảng đạt 3NF và không có khóa ứng viên gối nhau thì tự động đạt chuẩn BCNF.",
    "flashcard_front_vi": "Định nghĩa của Dạng chuẩn BCNF là gì?",
    "flashcard_back_vi": "Với mọi phụ thuộc hàm X -> Y không tầm thường, vế trái X bắt buộc phải là một Siêu khóa (Super Key)."
}

DATA_MOD_10_13[250] = {
    "prompt_vi": "Tên viết tắt đầy đủ của dạng chuẩn DKNF là gì?",
    "options_vi": {
        "A": "Donner-Korth Normal Form",
        "B": "Domain-Key Normal Form (Dạng chuẩn Miền-Khóa)",
        "C": "Dual-Key Normal Form",
        "D": "Domain-Knowledge Normal Form"
    },
    "explanation_vi": "`DKNF` là viết tắt của `Domain-Key Normal Form` (Dạng chuẩn Miền - Khóa). Một quan hệ ở dạng chuẩn DKNF nếu mọi ràng buộc trên quan hệ đó đều là hệ quả logic của các ràng buộc miền giá trị (domain constraints) và ràng buộc khóa (key constraints). Đây là dạng chuẩn cao nhất về mặt lý thuyết.",
    "key_takeaway_vi": "DKNF = Domain-Key Normal Form (Dạng chuẩn Miền-Khóa).",
    "flashcard_front_vi": "DKNF là viết tắt của cụm từ nào?",
    "flashcard_back_vi": "Domain-Key Normal Form (Dạng chuẩn Miền - Khóa)."
}

DATA_MOD_10_13[251] = {
    "prompt_vi": "Nếu một bảng được cho là đã đạt Dạng chuẩn 3 (3NF) thì điều nào sau đây CÓ THỂ KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Mỗi giao điểm giữa dòng và cột chỉ chứa duy nhất một giá trị thuộc miền xác định.",
        "B": "Bảng hoàn toàn không còn bất kỳ dị thường sửa đổi nào (The table is free of modification anomalies).",
        "C": "Mọi thuộc tính không khóa đều phụ thuộc trực tiếp (không bắc cầu) vào mọi khóa ứng viên.",
        "D": "Tất cả các thuộc tính không khóa đều phụ thuộc hàm vào toàn bộ mọi khóa ứng viên."
    },
    "explanation_vi": "Một bảng dù đã đạt 3NF vẫn CÓ THỂ còn dị thường sửa đổi (modification anomalies) nếu nó chứa các khóa ứng viên gối nhau (cần đưa lên BCNF), hoặc chứa phụ thuộc đa trị (cần 4NF), hoặc phụ thuộc nối (cần 5NF). Do đó phát biểu rằng bảng 3NF 'hoàn toàn không còn dị thường' là không đúng.",
    "key_takeaway_vi": "Bảng đạt 3NF vẫn có thể phát sinh dị thường nếu có khóa gối nhau hoặc phụ thuộc đa trị.",
    "flashcard_front_vi": "Tại sao bảng đạt chuẩn 3NF vẫn chưa hoàn hảo 100%?",
    "flashcard_back_vi": "Vì 3NF vẫn có thể gặp dị thường khi có khóa ứng viên chồng chéo (cần BCNF) hoặc phụ thuộc đa trị (cần 4NF)."
}

DATA_MOD_10_13[252] = {
    "prompt_vi": "Phát biểu nào sau đây mô tả chính xác nhất về các dị thường thao tác dữ liệu (modification anomalies)?",
    "options_vi": {
        "A": "Dị thường thao tác chỉ xuất hiện tối đa ở Dạng chuẩn 2.",
        "B": "Khi tồn tại dị thường thao tác, dữ liệu trong bảng hoàn toàn không thể chỉnh sửa.",
        "C": "Khi cố gắng thay đổi dữ liệu trong bảng, các tác dụng phụ ngoài ý muốn có thể xảy ra (undesired side-effects may follow).",
        "D": "Khi sửa đổi bảng, các lỗi hệ thống thường xuyên phát sinh do dị thường."
    },
    "explanation_vi": "Dị thường dữ liệu (Anomalies) là những tác dụng phụ không mong muốn khi thực hiện thao tác dữ liệu: Thêm mới bị thiếu thông tin khóa (Insertion anomaly), Cập nhật một chỗ nhưng quên chỗ khác dẫn đến mâu thuẫn (Update anomaly), hoặc Xóa một thông tin này vô tình làm mất luôn thông tin khác (Deletion anomaly).",
    "key_takeaway_vi": "Dị thường thao tác là các tác dụng phụ ngoài ý muốn (mất dữ liệu, mâu thuẫn dữ liệu) khi thêm/sửa/xóa.",
    "flashcard_front_vi": "3 loại dị thường thao tác dữ liệu chính trong CSDL là gì?",
    "flashcard_back_vi": "1. Insertion Anomaly (Dị thường thêm), 2. Deletion Anomaly (Dị thường xóa), 3. Update Anomaly (Dị thường sửa)."
}

DATA_MOD_10_13[253] = {
    "prompt_vi": "Mối quan hệ phụ thuộc nào sau đây chỉ ra rằng Y phụ thuộc bắc cầu vào X?",
    "options_vi": {
        "A": "X -> Y, Z -> X",
        "B": "X -> Y, Z -> X",
        "C": "Y -> Z, Z -> X",
        "D": "Z -> Y, X -> Z (X xác định Z, và Z xác định Y)"
    },
    "explanation_vi": "Định nghĩa phụ thuộc bắc cầu: Nếu `X -> Z` và `Z -> Y` (với Z không phải là siêu khóa và Y không phụ thuộc trực tiếp vào X), thì `Y` được gọi là phụ thuộc bắc cầu vào `X` thông qua thuộc tính trung gian `Z`.",
    "key_takeaway_vi": "Phụ thuộc bắc cầu: X -> Z và Z -> Y suy ra Y phụ thuộc bắc cầu vào X.",
    "flashcard_front_vi": "Công thức toán học của Phụ thuộc hàm bắc cầu là gì?",
    "flashcard_back_vi": "X -> Z và Z -> Y (X xác định Z, Z xác định Y, suy ra X gián tiếp xác định Y)."
}

DATA_MOD_10_13[254] = {
    "prompt_vi": "Tên gọi đầy đủ chính xác của dạng chuẩn BCNF là gì?",
    "options_vi": {
        "A": "Boyce-Cartesian normal form",
        "B": "Boyce-Codd normal form",
        "C": "Bond-Codd normal form",
        "D": "Borne-Codd normal form"
    },
    "explanation_vi": "BCNF được đặt theo tên của hai nhà khoa học máy tính tiên phong là Raymond F. Boyce và Edgar F. Codd (người cha đẻ của mô hình CSDL quan hệ).",
    "key_takeaway_vi": "BCNF = Boyce-Codd Normal Form.",
    "flashcard_front_vi": "BCNF mang tên của ai?",
    "flashcard_back_vi": "Raymond F. Boyce và Edgar F. Codd (Boyce-Codd Normal Form)."
}

DATA_MOD_10_13[255] = {
    "prompt_vi": "Thuật ngữ nào sau đây KHÔNG PHẢI là một loại dị thường thao tác dữ liệu (Modification anomaly) hợp lệ?",
    "options_vi": {
        "A": "Dị thường cập nhật (Update Anomaly)",
        "B": "Dị thường chèn thêm (Insertion anomaly)",
        "C": "Dị thường xóa (Deletion anomaly)",
        "D": "Dị thường drop (Drop anomaly)"
    },
    "explanation_vi": "Trong lý thuyết thiết kế cơ sở dữ liệu, chỉ có chính xác 3 loại dị thường dữ liệu kinh điển: 1. `Insertion Anomaly` (dị thường thêm); 2. `Deletion Anomaly` (dị thường xóa); và 3. `Update Anomaly` (dị thường cập nhật). Hoàn toàn không có khái niệm nào là 'Drop anomaly'.",
    "key_takeaway_vi": "3 loại dị thường dữ liệu: Insertion, Deletion, Update. Không có Drop anomaly.",
    "flashcard_front_vi": "Kể tên 3 dị thường dữ liệu kinh điển trong cơ sở dữ liệu?",
    "flashcard_back_vi": "Insertion Anomaly (thêm), Deletion Anomaly (xóa), và Update Anomaly (sửa)."
}

DATA_MOD_10_13[256] = {
    "prompt_vi": "Xem xét cấu trúc và dữ liệu bảng sau:\nFaculty ID, Faculty Name, Faculty Hire Date, Course Code\n(389, Dr. Giddens, 10-Feb-1985, ENG-206)\n(407, Dr. Saperstein, 19-Apr-1999, CMP-101)\n(407, Dr. Saperstein, 19-Apr-1999, CMP-201)\nNhững loại dị thường thao tác nào có thể xảy ra khi sửa đổi bảng này?",
    "options_vi": {
        "A": "Dị thường chèn, cập nhật và xóa (Insertion, Update and Deletion anomaly).",
        "B": "Chỉ có dị thường chèn.",
        "C": "Dị thường chèn và cập nhật.",
        "D": "Dị thường cập nhật và xóa."
    },
    "explanation_vi": "Bảng này kết hợp thông tin giảng viên và khóa học vào làm một: 1. `Insertion anomaly`: Không thể thêm giảng viên mới nếu người đó chưa dạy môn nào (vì Course Code là phần của khóa chính); 2. `Update anomaly`: Nếu Dr. Saperstein đổi ngày tuyển dụng, phải sửa ở nhiều dòng, dễ gây mâu thuẫn; 3. `Deletion anomaly`: Nếu xóa môn ENG-206, thông tin của Dr. Giddens cũng bị biến mất vĩnh viễn.",
    "key_takeaway_vi": "Bảng vi phạm chuẩn hóa sẽ cùng lúc mắc phải cả 3 dị thường: Thêm (Insert), Sửa (Update) và Xóa (Delete).",
    "flashcard_front_vi": "Bảng thiết kế kém thường mắc phải những dị thường nào?",
    "flashcard_back_vi": "Mắc phải đồng thời cả 3 dị thường: Insertion Anomaly, Update Anomaly, Deletion Anomaly."
}

DATA_MOD_10_13[257] = {
    "prompt_vi": "Điều nào sau đây KHÔNG PHẢI là một mục tiêu hợp lệ của chuẩn hóa cơ sở dữ liệu?",
    "options_vi": {
        "A": "Loại bỏ các dị thường thao tác dữ liệu.",
        "B": "Làm cho mô hình dữ liệu mang nhiều thông tin rõ ràng hơn cho người dùng.",
        "C": "Hoàn toàn tránh được việc phải thay đổi cấu trúc bảng sau khi chuẩn hóa (Completely avoid the need to change table structure).",
        "D": "Giảm thiểu việc phải thiết kế lại khi mở rộng cấu trúc cơ sở dữ liệu."
    },
    "explanation_vi": "Phát biểu C là SAI. Chuẩn hóa giúp tối ưu hóa cấu trúc và giảm thiểu thiết kế lại, nhưng không thể 'hoàn toàn tránh khỏi việc thay đổi cấu trúc bảng trong tương lai' vì các yêu cầu nghiệp vụ của doanh nghiệp luôn luôn thay đổi theo thời gian.",
    "key_takeaway_vi": "Chuẩn hóa không thể ngăn chặn 100% việc thay đổi cấu trúc bảng khi nghiệp vụ mở rộng.",
    "flashcard_front_vi": "Mục tiêu chính của chuẩn hóa là gì?",
    "flashcard_back_vi": "Giảm thiểu dư thừa, loại bỏ dị thường và tạo cấu trúc linh hoạt để mở rộng nghiệp vụ."
}

DATA_MOD_10_13[258] = {
    "prompt_vi": "Xét cấu trúc bảng Transactions:\nCustomer, Tr. ID, Date, Amount\nJones có 2 giao dịch (12890 và 12904), Stevens có 3 giao dịch...\nBảng này đang ở dạng chuẩn nào?",
    "options_vi": {
        "A": "3NF",
        "B": "1NF",
        "C": "2NF",
        "D": "Chưa đạt dạng chuẩn 1 (Non 1NF)"
    },
    "explanation_vi": "Nhìn vào dữ liệu bảng: Dưới tên khách hàng 'Jones' có 2 giao dịch liên tiếp mà ô Customer ở dòng 2 bị để trống (nhóm lặp - Repeating Group), hoặc hiểu là một ô khách hàng chứa một danh sách nhiều giao dịch. Điều này vi phạm tính nguyên tử (Atomicity) của thuộc tính. Vì vậy bảng `CHƯA ĐẠT DẠNG CHUẨN 1 (Non 1NF)`.",
    "key_takeaway_vi": "Bảng có nhóm lặp hoặc một ô chứa nhiều giá trị là Non-1NF (chưa đạt 1NF).",
    "flashcard_front_vi": "Tại sao bảng chứa nhóm lặp (repeating group) lại là Non-1NF?",
    "flashcard_back_vi": "Vì 1NF yêu cầu mọi ô dữ liệu tại giao điểm hàng và cột phải chứa giá trị nguyên tử (Atomic/đơn trị)."
}

DATA_MOD_10_13[259] = {
    "prompt_vi": "Phụ thuộc hàm (Functional dependency) là gì?",
    "options_vi": {
        "A": "Mỗi giá trị X gắn với nhiều hơn một giá trị Y.",
        "B": "Mỗi giá trị Y gắn với duy nhất một giá trị X.",
        "C": "Thuộc tính Y có phụ thuộc hàm vào tập thuộc tính X nếu và chỉ nếu mỗi giá trị X gắn liền với DUY NHẤT MỘT giá trị Y (precisely one Y value).",
        "D": "Mỗi giá trị X gắn với ít nhất một giá trị Y."
    },
    "explanation_vi": "Định nghĩa toán học của Phụ thuộc hàm (`X -> Y`): Thuộc tính Y phụ thuộc hàm vào X nếu với bất kỳ hai dòng nào có cùng giá trị X (`t1[X] = t2[X]`), chúng bắt buộc phải có cùng giá trị Y (`t1[Y] = t2[Y]`). Nghĩa là biết X thì xác định được duy nhất một giá trị Y.",
    "key_takeaway_vi": "Phụ thuộc hàm X -> Y nghĩa là ứng với mỗi giá trị X chỉ có duy nhất một giá trị Y tương ứng.",
    "flashcard_front_vi": "Định nghĩa chuẩn của Phụ thuộc hàm X -> Y?",
    "flashcard_back_vi": "Mỗi giá trị của X xác định duy nhất chính xác một giá trị của Y."
}

DATA_MOD_10_13[260] = {
    "prompt_vi": "Ký hiệu X -> Y có ý nghĩa gì về hai thuộc tính X và Y?",
    "options_vi": {
        "A": "X phụ thuộc hàm vào Y.",
        "B": "Y phụ thuộc hàm vào X (Y is functionally dependent on X).",
        "C": "Không câu nào đúng.",
        "D": "X và Y phụ thuộc hàm lẫn nhau."
    },
    "explanation_vi": "Ký hiệu toán học `X -> Y` được đọc là: 'X xác định hàm Y' (X functionally determines Y) hoặc 'Y phụ thuộc hàm vào X' (Y is functionally dependent on X). X là thuộc tính định danh (Determinant), Y là thuộc tính phụ thuộc.",
    "key_takeaway_vi": "X -> Y nghĩa là Y phụ thuộc hàm vào X (X xác định Y).",
    "flashcard_front_vi": "Ký hiệu X -> Y phát biểu bằng lời như thế nào?",
    "flashcard_back_vi": "Y phụ thuộc hàm vào X (hoặc X xác định hàm Y)."
}

print(f"Loaded {len(DATA_MOD_10_13)} questions for Modules 10-13.")
