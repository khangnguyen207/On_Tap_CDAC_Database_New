# -*- coding: utf-8 -*-
"""
Module 7 (Q121-Q140), Module 8 (Q141-Q160), Module 9 (Q161-Q180)
Comprehensive Bilingual Translations & Lecturer Explanations
"""

DATA_MOD_7_9 = {}

# MODULE 7: Group Functions (Q121 - Q140)
DATA_MOD_7_9[121] = {
    "prompt_vi": "Phát biểu nào sau đây là ĐÚNG khi nói về các mệnh đề WHERE và HAVING?",
    "options_vi": {
        "A": "Mệnh đề HAVING chỉ có thể được dùng để giới hạn các nhóm (restrict groups only).",
        "B": "Mệnh đề WHERE chỉ có thể được dùng để giới hạn các nhóm.",
        "C": "Mệnh đề WHERE có thể được dùng để giới hạn cả dòng đơn lẻ và các nhóm.",
        "D": "Mệnh đề HAVING có thể được dùng để giới hạn cả dòng đơn lẻ và các nhóm (restrict both rows and groups)."
    },
    "explanation_vi": "Về mặt kỹ thuật SQL: Mệnh đề WHERE chỉ lọc từng dòng dữ liệu TRƯỚC KHI gom nhóm (không thể chứa hàm nhóm). Mệnh đề HAVING được thiết kế để lọc các nhóm SAU KHI gom nhóm, nhưng nó cũng có thể chứa các điều kiện lọc cột không gom nhóm (lọc dòng). Do đó HAVING có khả năng lọc cả dòng và nhóm (mặc dù lọc dòng ở WHERE tối ưu hiệu năng hơn rất nhiều).",
    "key_takeaway_vi": "WHERE chỉ lọc từng dòng trước khi gom nhóm; HAVING lọc các nhóm sau khi GROUP BY (và có thể lọc cả dòng).",
    "flashcard_front_vi": "Sự khác biệt cốt lõi giữa WHERE và HAVING trong SQL là gì?",
    "flashcard_back_vi": "WHERE lọc từng dòng trước khi GROUP BY (không được chứa hàm nhóm). HAVING lọc sau khi GROUP BY (chứa được hàm nhóm)."
}

DATA_MOD_7_9[122] = {
    "prompt_vi": "Bảng EMPLOYEES có các cột: EMP_ID, LAST_NAME, FIRST_NAME, DEPT_ID.\nCâu lệnh nào sau đây đếm số lượng các phòng ban KHÁC NHAU có nhân viên mang họ 'Smith'?",
    "options_vi": {
        "A": "SELECT DISTINCT(COUNT(dept_id)) FROM employees WHERE last_name='Smith';",
        "B": "SELECT COUNT(*) FROM employees WHERE last_name='Smith';",
        "C": "SELECT COUNT(DISTINCT dept_id) FROM employees WHERE last_name='Smith';",
        "D": "SELECT COUNT (dept_id) FROM employees WHERE last_name='Smith';"
    },
    "explanation_vi": "Để đếm số lượng giá trị không trùng lặp, từ khóa `DISTINCT` phải được đặt BÊN TRONG dấu ngoặc của hàm đếm: `COUNT(DISTINCT dept_id)`. Nếu viết `DISTINCT(COUNT(...))` thì hàm COUNT sẽ đếm hết rồi mới áp dụng DISTINCT trên con số duy nhất đó, hoàn toàn vô nghĩa.",
    "key_takeaway_vi": "Đếm số lượng giá trị phân biệt: COUNT(DISTINCT column_name).",
    "flashcard_front_vi": "Cú pháp đếm số lượng giá trị không trùng lặp trong một cột?",
    "flashcard_back_vi": "COUNT(DISTINCT column_name)."
}

DATA_MOD_7_9[123] = {
    "prompt_vi": "Điều nào sau đây là ĐÚNG khi sử dụng các hàm nhóm (group functions) trên các cột có chứa giá trị NULL?",
    "options_vi": {
        "A": "Các hàm nhóm trên cột kiểu ngày tháng sẽ bao gồm cả giá trị NULL.",
        "B": "Các hàm nhóm trên các cột sẽ TỰ ĐỘNG BỎ QUA các giá trị NULL (ignore NULL values).",
        "C": "Hàm nhóm không thể sử dụng chính xác trên cột có chứa giá trị NULL.",
        "D": "Các hàm nhóm trên cột kiểu số sẽ bao gồm cả giá trị NULL."
    },
    "explanation_vi": "Quy tắc bất biến của SQL: Tất cả các hàm nhóm (SUM, AVG, MIN, MAX, COUNT(cột)) đều TỰ ĐỘNG BỎ QUA (ignore) các giá trị NULL khi tính toán. Duy nhất chỉ có hàm `COUNT(*)` là đếm tất cả các dòng bao gồm cả các dòng có cột chứa NULL.",
    "key_takeaway_vi": "Các hàm nhóm tự động bỏ qua NULL. Riêng COUNT(*) đếm cả dòng chứa NULL.",
    "flashcard_front_vi": "Hàm nhóm (SUM, AVG, COUNT(col)) xử lý giá trị NULL như thế nào?",
    "flashcard_back_vi": "Tự động bỏ qua (ignore) các giá trị NULL. Chỉ có COUNT(*) đếm tất cả các dòng."
}

DATA_MOD_7_9[124] = {
    "prompt_vi": "Bảng STUDENT_GRADES có: STUDENT_ID, SEMESTER_END, GPA.\nCâu lệnh nào sau đây tìm điểm trung bình tích lũy (GPA) cao nhất theo từng học kỳ (per semester)?",
    "options_vi": {
        "A": "SELECT MAX(gpa) FROM student_grades WHERE gpa IS NOT NULL GROUP BY semester_end;",
        "B": "SELECT (gpa) FROM student_grades GROUP BY semester_end WHERE gpa IS NOT NULL",
        "C": "SELECT MAX(gpa) FROM student_grades WHERE gpa IS NOT NULL",
        "D": "SELECT MAX(gpa) GROUP BY semester_end WHERE gpa IS NOT NULL FROM student_grades"
    },
    "explanation_vi": "Để tính theo từng học kỳ, bắt buộc phải có mệnh đề `GROUP BY semester_end`. Thứ tự các mệnh đề chuẩn trong SQL: `SELECT ... FROM ... WHERE ... GROUP BY ...`. Do đó phương án A là chính xác.",
    "key_takeaway_vi": "Tính giá trị lớn nhất theo từng nhóm: SELECT MAX(col) FROM table GROUP BY group_col;",
    "flashcard_front_vi": "Thứ tự đúng của các mệnh đề SELECT, FROM, WHERE, GROUP BY là gì?",
    "flashcard_back_vi": "SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY."
}

DATA_MOD_7_9[125] = {
    "prompt_vi": "Những kiểu dữ liệu nào sau đây tương thích để áp dụng các hàm nhóm như MIN và MAX?",
    "options_vi": {
        "A": "Kiểu số (Numeric)",
        "B": "Kiểu ngày tháng (Date)",
        "C": "Tất cả các kiểu trên (All of the above - Numeric, Date, Character)",
        "D": "Kiểu chuỗi ký tự (Character)"
    },
    "explanation_vi": "Các hàm `MIN` và `MAX` có thể áp dụng cho MỌI kiểu dữ liệu có thể so sánh thứ tự: Số (nhỏ nhất/lớn nhất), Ngày tháng (sớm nhất/muộn nhất), và Chuỗi ký tự (thứ tự chữ cái A-Z). Ngược lại, hàm `SUM` và `AVG` chỉ áp dụng được duy nhất cho kiểu số.",
    "key_takeaway_vi": "MIN và MAX áp dụng được cho cả Kiểu Số, Kiểu Ngày và Kiểu Chuỗi. SUM và AVG chỉ dùng cho Kiểu Số.",
    "flashcard_front_vi": "Hàm MIN và MAX có dùng được cho kiểu chuỗi và ngày tháng không?",
    "flashcard_back_vi": "CÓ. Dùng được cho cả số, chuỗi (thứ tự từ điển) và ngày tháng (thời gian sớm/muộn)."
}

DATA_MOD_7_9[126] = {
    "prompt_vi": "Cách viết nào sau đây KHÔNG PHẢI là một biến thể hợp lệ của hàm COUNT?",
    "options_vi": {
        "A": "COUNT(*)",
        "B": "COUNT(expr1, expr2)",
        "C": "COUNT(DISTINCT expr)",
        "D": "COUNT(expr)"
    },
    "explanation_vi": "Hàm `COUNT` trong SQL chỉ chấp nhận duy nhất MỘT đối số (hoặc dấu `*`). Cú pháp `COUNT(expr1, expr2)` với 2 đối số là hoàn toàn sai cú pháp.",
    "key_takeaway_vi": "Hàm COUNT chỉ nhận 1 tham số duy nhất hoặc dấu *; không chấp nhận 2 tham số.",
    "flashcard_front_vi": "Hàm COUNT có nhận 2 tham số: COUNT(col1, col2) được không?",
    "flashcard_back_vi": "KHÔNG. Hàm COUNT chỉ nhận 1 đối số: COUNT(*), COUNT(col), hoặc COUNT(DISTINCT col)."
}

DATA_MOD_7_9[127] = {
    "prompt_vi": "Câu lệnh nào sau đây tính tỷ lệ phần trăm hoa hồng trung bình (Average commission percentage) từ bảng employees bằng cách coi các giá trị NULL là số 0?",
    "options_vi": {
        "A": "SELECT AVG(NVL(commission_pct, 0)) FROM employees",
        "B": "SELECT NULLIF(AVG(commission_pct), 0) FROM employees",
        "C": "SELECT AVG(NULLIF(commission_pct, 0)) FROM employees",
        "D": "SELECT NVL(AVG(commission_pct), 0) FROM employees"
    },
    "explanation_vi": "Mặc định hàm `AVG(commission_pct)` sẽ bỏ qua các dòng có hoa hồng là NULL (tổng hoa hồng chia cho số nhân viên CÓ hoa hồng). Muốn tính trung bình trên TOÀN BỘ nhân viên (coi người không có hoa hồng là 0%), ta bắt buộc phải dùng `NVL(commission_pct, 0)` bên trong hàm AVG.",
    "key_takeaway_vi": "Để hàm AVG tính cả các dòng NULL như số 0, bắt buộc viết: AVG(NVL(column, 0)).",
    "flashcard_front_vi": "Sự khác biệt giữa AVG(commission_pct) và AVG(NVL(commission_pct, 0))?",
    "flashcard_back_vi": "AVG(col) chia cho số dòng khác NULL. AVG(NVL(col,0)) chia cho tổng số dòng (coi NULL là 0)."
}

DATA_MOD_7_9[128] = {
    "prompt_vi": "Câu lệnh nào sau đây sẽ BỊ LỖI khi thực thi?",
    "options_vi": {
        "A": "SELECT AVG(salary) FROM employees GROUP BY department_id",
        "B": "SELECT department_id, AVG(salary) FROM employees GROUP BY department_id",
        "C": "SELECT job_id, AVG(salary) FROM employees GROUP BY department_id",
        "D": "SELECT AVG(salary), job_id FROM employees GROUP BY department_id, job_id"
    },
    "explanation_vi": "🔥 QUY TẮC BẤT DI BẤT DỊCH CỦA GROUP BY: Bất kỳ cột đơn lẻ nào xuất hiện trong mệnh đề `SELECT` mà KHÔNG nằm bên trong một hàm nhóm thì BẮT BUỘC phải có mặt trong mệnh đề `GROUP BY`. Ở câu C, `job_id` có trong SELECT nhưng không có trong GROUP BY nên Oracle báo lỗi `ORA-00979: not a GROUP BY expression`.",
    "key_takeaway_vi": "Cột không phải hàm nhóm trong SELECT bắt buộc phải xuất hiện trong GROUP BY.",
    "flashcard_front_vi": "Nguyên nhân gây ra lỗi ORA-00979 'not a GROUP BY expression'?",
    "flashcard_back_vi": "Liệt kê cột trong mệnh đề SELECT mà không đặt cột đó vào mệnh đề GROUP BY (và không bọc trong hàm nhóm)."
}

DATA_MOD_7_9[129] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Bạn không thể sử dụng mệnh đề WHERE để giới hạn (lọc) các nhóm.",
        "B": "Bạn có thể sử dụng các hàm nhóm trong mệnh đề WHERE (You can use group functions in the WHERE clause).",
        "C": "Bạn không thể sử dụng các hàm nhóm trong mệnh đề WHERE.",
        "D": "Bạn sử dụng mệnh đề HAVING để giới hạn các nhóm."
    },
    "explanation_vi": "Các hàm nhóm (SUM, AVG, COUNT, MIN, MAX...) TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP xuất hiện trong mệnh đề `WHERE`. Muốn lọc dựa trên kết quả của hàm nhóm, bắt buộc phải dùng mệnh đề `HAVING`. Do đó phát biểu B là SAI.",
    "key_takeaway_vi": "Hàm nhóm không bao giờ được xuất hiện trong mệnh đề WHERE. Phải dùng HAVING để lọc hàm nhóm.",
    "flashcard_front_vi": "Có được viết WHERE AVG(salary) > 5000 không?",
    "flashcard_back_vi": "KHÔNG. Tuyệt đối không dùng hàm nhóm trong WHERE. Phải viết: HAVING AVG(salary) > 5000."
}

DATA_MOD_7_9[130] = {
    "prompt_vi": "Câu lệnh nào sau đây hiển thị số lượng các giá trị phòng ban khác nhau (distinct department values) trong bảng EMPLOYEES?",
    "options_vi": {
        "A": "SELECT COUNT(department_id) FROM employees",
        "B": "SELECT DISTINCT COUNT(department_id) FROM employees",
        "C": "SELECT COUNT(DISTINCT department_id) FROM employees",
        "D": "SELECT DISTINCT department_id FROM employees;"
    },
    "explanation_vi": "Để đếm số lượng các giá trị phòng ban duy nhất không trùng lặp, cú pháp chính xác là `SELECT COUNT(DISTINCT department_id) FROM employees;`.",
    "key_takeaway_vi": "Đếm số lượng giá trị phân biệt: COUNT(DISTINCT col).",
    "flashcard_front_vi": "Hàm đếm số giá trị phân biệt trong một cột?",
    "flashcard_back_vi": "COUNT(DISTINCT column_name)."
}

DATA_MOD_7_9[131] = {
    "prompt_vi": "Kết quả của câu lệnh sau là gì?\nSELECT department_id, AVG(salary) FROM employees WHERE AVG(salary) > 8000 GROUP BY department_id;",
    "options_vi": {
        "A": "Hiển thị mã phòng ban và lương trung bình của nhân viên.",
        "B": "Hiển thị danh sách phòng ban và lương trung bình của từng phòng.",
        "C": "Chỉ hiển thị các phòng ban có lương trung bình lớn hơn 8000.",
        "D": "Câu lệnh sẽ trả về thông báo lỗi (The statement will return an error)."
    },
    "explanation_vi": "Câu lệnh bị lỗi `ORA-00934: group function is not allowed here` vì hàm nhóm `AVG(salary)` được sử dụng trái phép trong mệnh đề `WHERE`. Muốn lọc lương trung bình > 8000, bắt buộc phải dùng `HAVING AVG(salary) > 8000` đặt sau mệnh đề GROUP BY.",
    "key_takeaway_vi": "Viết hàm nhóm trong WHERE luôn luôn sinh lỗi ORA-00934.",
    "flashcard_front_vi": "Tại sao SELECT ... WHERE AVG(salary) > 8000 GROUP BY ... bị lỗi?",
    "flashcard_back_vi": "Vì hàm nhóm (AVG) không được phép nằm trong mệnh đề WHERE. Phải chuyển sang HAVING."
}

DATA_MOD_7_9[132] = {
    "prompt_vi": "Bảng STUDENTS có cột START_DATE kiểu DATE. Hàm tổng hợp nào sau đây là hợp lệ trên cột START_DATE?",
    "options_vi": {
        "A": "MIN(start_date)",
        "B": "AVG(start_date)",
        "C": "MAXIMUM(start_date)",
        "D": "SUM(start_date)"
    },
    "explanation_vi": "Trên kiểu dữ liệu ngày tháng (DATE), chỉ có các hàm `MIN` (ngày sớm nhất), `MAX` (ngày muộn nhất) và `COUNT` là hợp lệ. Các hàm `AVG` và `SUM` chỉ áp dụng cho kiểu số. Cú pháp 'MAXIMUM' không tồn tại trong SQL.",
    "key_takeaway_vi": "Cột ngày tháng chỉ áp dụng được MIN, MAX, COUNT; không dùng được AVG hay SUM.",
    "flashcard_front_vi": "Cột kiểu DATE có tính được AVG hay SUM không?",
    "flashcard_back_vi": "KHÔNG. AVG và SUM chỉ dùng cho số. Cột DATE chỉ dùng được MIN, MAX và COUNT."
}

DATA_MOD_7_9[133] = {
    "prompt_vi": "Điều gì là ĐÚNG về câu lệnh sau?\nSELECT MAX(AVG(salary)) FROM employees GROUP BY department_id;",
    "options_vi": {
        "A": "Sẽ báo lỗi vì các hàm nhóm không thể lồng nhau.",
        "B": "Sẽ trả về lương trung bình lớn nhất cho từng phòng ban.",
        "C": "Sẽ báo lỗi vì Salary không có trong mệnh đề group by.",
        "D": "Sẽ hiển thị giá trị lớn nhất trong số các mức lương trung bình của các phòng ban (maximum of average salaries)."
    },
    "explanation_vi": "Trong Oracle SQL, các hàm nhóm ĐƯỢC PHÉP LỒNG NHAU TỐI ĐA 2 CẤP khi có mệnh đề `GROUP BY`. `AVG(salary)` tính lương trung bình của từng phòng ban, sau đó `MAX(...)` lấy ra con số trung bình cao nhất trong tất cả các phòng ban đó và trả về duy nhất 1 dòng.",
    "key_takeaway_vi": "Oracle cho phép lồng hàm nhóm tối đa 2 cấp (ví dụ MAX(AVG(salary))) khi có GROUP BY.",
    "flashcard_front_vi": "Hàm nhóm trong Oracle có thể lồng nhau tối đa mấy cấp?",
    "flashcard_back_vi": "Tối đa 2 cấp (ví dụ: MAX(AVG(salary)) GROUP BY dept_id)."
}

DATA_MOD_7_9[134] = {
    "prompt_vi": "Bảng MARKS có STD_ID, STUDENT_NAME, SUBJ1, SUBJ2. Đánh giá câu lệnh:\nSELECT subj1+subj2 total_marks, std_id FROM marks WHERE subj1 > AVG(subj1) AND subj2 > AVG(subj2) ORDER BY total_marks;\nKết quả của câu lệnh SELECT là gì?",
    "options_vi": {
        "A": "Câu lệnh báo lỗi tại mệnh đề WHERE (returns an error at the WHERE clause).",
        "B": "Thực thi thành công và hiển thị kết quả.",
        "C": "Báo lỗi tại mệnh đề SELECT.",
        "D": "Báo lỗi tại mệnh đề ORDER BY."
    },
    "explanation_vi": "Mệnh đề `WHERE` chứa các hàm nhóm `AVG(subj1)` và `AVG(subj2)` mà không dùng qua subquery, điều này vi phạm nghiêm trọng cú pháp SQL và gây ra lỗi trực tiếp tại mệnh đề WHERE.",
    "key_takeaway_vi": "Hàm nhóm không được đứng trực tiếp trong WHERE, muốn so sánh phải dùng subquery: WHERE col > (SELECT AVG...).",
    "flashcard_front_vi": "Làm sao để so sánh cột với giá trị trung bình trong WHERE?",
    "flashcard_back_vi": "Bắt buộc dùng subquery: WHERE subj1 > (SELECT AVG(subj1) FROM marks)."
}

DATA_MOD_7_9[135] = {
    "prompt_vi": "Phát biểu nào sau đây là ĐÚNG về các hàm tổng hợp (aggregate functions)?",
    "options_vi": {
        "A": "Bạn có thể kết hợp các cột đơn dòng với hàm tổng hợp trong danh sách SELECT bằng cách gom nhóm theo các cột đơn dòng đó trong GROUP BY.",
        "B": "Bạn chỉ có thể dùng hàm tổng hợp trong danh sách cột SELECT và trong mệnh đề WHERE.",
        "C": "Bạn chỉ có thể dùng hàm tổng hợp trên bảng bằng cách gom toàn bộ bảng thành 1 nhóm duy nhất.",
        "D": "Bạn có thể dùng hàm tổng hợp trong bất kỳ mệnh đề nào của câu lệnh SELECT."
    },
    "explanation_vi": "Muốn hiển thị một cột thông thường cùng với một hàm nhóm trong SELECT, cột đó BẮT BUỘC phải được đưa vào mệnh đề `GROUP BY`. Đó chính là quy tắc phối hợp giữa cột đơn lẻ và hàm nhóm.",
    "key_takeaway_vi": "Cột đơn dòng muốn đứng cạnh hàm nhóm trong SELECT thì phải được gom nhóm trong GROUP BY.",
    "flashcard_front_vi": "Điều kiện để chọn một cột đơn dòng cùng với hàm tổng hợp là gì?",
    "flashcard_back_vi": "Cột đơn dòng đó bắt buộc phải nằm trong mệnh đề GROUP BY."
}

DATA_MOD_7_9[136] = {
    "prompt_vi": "Mệnh đề nào sau đây bạn nên sử dụng để loại trừ (lọc bớt) các kết quả nhóm?",
    "options_vi": {
        "A": "HAVING",
        "B": "RESTRICT",
        "C": "WHERE",
        "D": "GROUP BY"
    },
    "explanation_vi": "Mệnh đề `HAVING` là mệnh đề chuyên biệt dùng để thiết lập điều kiện lọc bỏ các nhóm không thỏa mãn sau khi đã thực hiện phép gom nhóm (`GROUP BY`).",
    "key_takeaway_vi": "Để lọc điều kiện trên nhóm kết quả, dùng mệnh đề HAVING.",
    "flashcard_front_vi": "Mệnh đề nào dùng để lọc các nhóm sau khi gom nhóm?",
    "flashcard_back_vi": "Mệnh đề HAVING."
}

DATA_MOD_7_9[137] = {
    "prompt_vi": "Trong một câu lệnh SELECT có chứa mệnh đề WHERE, mệnh đề GROUP BY phải được đặt ở vị trí nào?",
    "options_vi": {
        "A": "Trước mệnh đề WHERE",
        "B": "Sau mệnh đề ORDER BY",
        "C": "Ngay sau mệnh đề SELECT",
        "D": "Sau mệnh đề WHERE (After the WHERE clause)"
    },
    "explanation_vi": "Thứ tự các mệnh đề chuẩn trong câu lệnh SQL: `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...`. Do đó `GROUP BY` bắt buộc phải đặt SAU mệnh đề `WHERE`.",
    "key_takeaway_vi": "GROUP BY luôn đứng sau WHERE và đứng trước HAVING / ORDER BY.",
    "flashcard_front_vi": "Vị trí của GROUP BY so với WHERE và HAVING?",
    "flashcard_back_vi": "GROUP BY đứng SAU WHERE và đứng TRƯỚC HAVING."
}

DATA_MOD_7_9[138] = {
    "prompt_vi": "Bảng EVENT có: EVENT_ID, EVENT_NAME, EVENT_DESC, EVENT_TYPE, LOCATION_ID.\nBạn cần báo cáo số lượng các loại sự kiện khác nhau (number of different event types) tại mỗi địa điểm (location). Câu lệnh nào đúng?",
    "options_vi": {
        "A": "SELECT COUNT(*), DISTINCT(location_id) FROM event;",
        "B": "SELECT location_id, COUNT(DISTINCT event_type) FROM event GROUP BY location_id;",
        "C": "SELECT DISTINCT (event_type) FROM event GROUP BY location_id;",
        "D": "SELECT UNIQUE(location_id), COUNT(event_type) FROM event GROUP BY location_id;"
    },
    "explanation_vi": "'Tại mỗi địa điểm' đòi hỏi gom nhóm theo `GROUP BY location_id`. 'Số lượng các loại sự kiện khác nhau' đòi hỏi đếm phân biệt `COUNT(DISTINCT event_type)`. Cú pháp B là hoàn toàn chính xác.",
    "key_takeaway_vi": "Số lượng loại khác nhau tại mỗi nhóm: SELECT group_col, COUNT(DISTINCT type_col) ... GROUP BY group_col;",
    "flashcard_front_vi": "Cách đếm số lượng phần tử phân biệt theo từng nhóm?",
    "flashcard_back_vi": "SELECT nhóm, COUNT(DISTINCT phân_loại) FROM bảng GROUP BY nhóm;"
}

DATA_MOD_7_9[139] = {
    "prompt_vi": "Phát biểu nào sau đây về thứ tự thực thi (evaluation) các mệnh đề trong câu lệnh SELECT là ĐÚNG?",
    "options_vi": {
        "A": "Oracle Server thực thi ORDER BY trước WHERE.",
        "B": "Oracle Server thực thi mệnh đề WHERE trước mệnh đề GROUP BY.",
        "C": "Oracle Server thực thi ORDER BY trước HAVING.",
        "D": "Oracle Server thực thi HAVING trước WHERE."
    },
    "explanation_vi": "Thứ tự thực thi luận lý (Logical Query Processing) của SQL Server / Oracle: 1. `FROM` -> 2. `WHERE` (lọc dòng thô) -> 3. `GROUP BY` (gom nhóm) -> 4. `HAVING` (lọc nhóm) -> 5. `SELECT` (chiếu cột) -> 6. `ORDER BY` (sắp xếp). Do đó WHERE luôn được thực thi trước GROUP BY.",
    "key_takeaway_vi": "Thứ tự thực thi logic: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY.",
    "flashcard_front_vi": "Mệnh đề WHERE được thực thi trước hay sau GROUP BY?",
    "flashcard_back_vi": "Thực thi TRƯỚC GROUP BY để lọc bớt các dòng dữ liệu không đạt yêu cầu trước khi gom nhóm."
}

DATA_MOD_7_9[140] = {
    "prompt_vi": "Bạn cần tính tổng tất cả tiền lương của nhân viên trong phòng kế toán (accounting department). Bạn nên dùng hàm nhóm nào?",
    "options_vi": {
        "A": "COUNT",
        "B": "MAX",
        "C": "MIN",
        "D": "SUM"
    },
    "explanation_vi": "Hàm tính tổng các giá trị số trong SQL là hàm `SUM()`. COUNT dùng để đếm số dòng, MAX tìm giá trị lớn nhất, MIN tìm giá trị nhỏ nhất.",
    "key_takeaway_vi": "Hàm tính tổng trong SQL là SUM.",
    "flashcard_front_vi": "Hàm nào tính tổng giá trị của một cột số?",
    "flashcard_back_vi": "Hàm SUM(column_name)."
}

# MODULE 8: SQL Joins (Q141 - Q160)
DATA_MOD_7_9[141] = {
    "prompt_vi": "Trong trường hợp nào sau đây bạn sẽ sử dụng phép kết nối FULL OUTER JOIN?",
    "options_vi": {
        "A": "Bạn muốn lấy tất cả dữ liệu không khớp từ một bảng duy nhất.",
        "B": "Bạn muốn lấy tất cả dữ liệu không khớp từ CẢ HAI BẢNG (all unmatched data from both tables).",
        "C": "Cả hai bảng đều có chứa giá trị NULL.",
        "D": "Bạn muốn lấy tất cả dữ liệu khớp từ cả hai bảng."
    },
    "explanation_vi": "`FULL OUTER JOIN` kết hợp kết quả của cả LEFT OUTER JOIN và RIGHT OUTER JOIN. Nó trả về tất cả các dòng khớp nhau, đồng thời giữ lại cả các dòng không khớp từ bảng bên trái VÀ các dòng không khớp từ bảng bên phải (điền NULL vào các cột thiếu).",
    "key_takeaway_vi": "FULL OUTER JOIN trả về toàn bộ dữ liệu khớp và không khớp từ cả hai bảng.",
    "flashcard_front_vi": "FULL OUTER JOIN trả về những dòng nào?",
    "flashcard_back_vi": "Trả về các dòng khớp nhau + các dòng không khớp từ bảng trái + các dòng không khớp từ bảng phải."
}

DATA_MOD_7_9[142] = {
    "prompt_vi": "Kết quả của câu truy vấn sau sẽ là gì?\nSELECT * FROM employees, departments;",
    "options_vi": {
        "A": "Hiển thị các dòng từ bảng employees trước, sau đó nối tiếp các dòng từ bảng departments.",
        "B": "Mặc định tự động nối 2 bảng theo department_id vì đây là khóa ngoại.",
        "C": "Tạo ra một tích Descartes (Cartesian product) do không chỉ định điều kiện kết nối (joining condition).",
        "D": "Báo lỗi vì thiếu điều kiện kết nối."
    },
    "explanation_vi": "Khi liệt kê nhiều bảng trong mệnh đề `FROM` mà hoàn toàn KHÔNG CÓ điều kiện kết nối (trong WHERE hoặc ON), cơ sở dữ liệu sẽ thực hiện phép nhân Descartes (Cartesian Product): mỗi dòng của bảng thứ nhất sẽ ghép đôi với mọi dòng của bảng thứ hai. Số dòng kết quả = số dòng bảng 1 * số dòng bảng 2.",
    "key_takeaway_vi": "Nối bảng mà quên điều kiện kết nối sẽ tạo ra tích Descartes (Cartesian Product).",
    "flashcard_front_vi": "Điều gì xảy ra khi viết SELECT * FROM table1, table2 mà không có WHERE?",
    "flashcard_back_vi": "Sinh ra tích Descartes (Cartesian Product): nhân toàn bộ số hàng của 2 bảng với nhau."
}

DATA_MOD_7_9[143] = {
    "prompt_vi": "Câu truy vấn nào sau đây tạo ra kết quả giống hệt như câu lệnh dưới đây?\nSELECT last_name, department_name FROM employees CROSS JOIN departments;",
    "options_vi": {
        "A": "SELECT last_name, department_name FROM employees e, departments d WHERE e.depatment_id (+) = d.department_id (+);",
        "B": "SELECT last_name, department_name FROM employees JOIN departments USING (department_id)",
        "C": "SELECT last_name, department_name FROM employees e, departments d WHERE e.depatment_id = d.department_id;",
        "D": "SELECT last_name, department_name FROM employees e, departments d;"
    },
    "explanation_vi": "`CROSS JOIN` là cú pháp chuẩn SQL:1999 để thực hiện phép nhân Descartes giữa 2 bảng. Trong cú pháp truyền thống của Oracle, phép nhân Descartes được viết đơn giản bằng cách liệt kê 2 bảng cách nhau bằng dấu phẩy trong mệnh đề FROM mà không có WHERE: `FROM employees e, departments d;`.",
    "key_takeaway_vi": "CROSS JOIN theo chuẩn SQL-99 tương đương với cú pháp truyền thống FROM table1, table2 không có WHERE.",
    "flashcard_front_vi": "Cú pháp truyền thống tương đương với CROSS JOIN là gì?",
    "flashcard_back_vi": "SELECT ... FROM table1, table2; (không có mệnh đề WHERE)."
}

DATA_MOD_7_9[144] = {
    "prompt_vi": "Ký hiệu nào sau đây là ký hiệu của phép nối ngoài (outer join) trong cú pháp truyền thống của Oracle?",
    "options_vi": {
        "A": "[+]",
        "B": "(+)",
        "C": "{+}",
        "D": "+"
    },
    "explanation_vi": "Trong cú pháp SQL độc quyền truyền thống của Oracle, toán tử kết nối ngoài được ký hiệu là `(+)`. Dấu `(+)` được đặt ở phía bảng bị thiếu dữ liệu (thiếu dòng) để yêu cầu Oracle tự động bù các dòng NULL.",
    "key_takeaway_vi": "Toán tử nối ngoài truyền thống của Oracle là (+).",
    "flashcard_front_vi": "Toán tử nối ngoài truyền thống của Oracle là gì?",
    "flashcard_back_vi": "(+) đặt bên phía bảng thiếu dữ liệu."
}

DATA_MOD_7_9[145] = {
    "prompt_vi": "Kết quả của câu lệnh sau sẽ là gì?\nSELECT e.last_name, e.department_id, d.department_name\nFROM employees e, departments d\nWHERE e.department_id(+) = d.department_id;",
    "options_vi": {
        "A": "Hiển thị thông tin cho tất cả nhân viên bất kể có phòng ban hay không.",
        "B": "Chỉ hiển thị thông tin khi có phòng ban khớp.",
        "C": "Hiển thị thông tin nhân viên cho tất cả nhân viên và phòng ban cho tất cả phòng ban.",
        "D": "Hiển thị tất cả nhân viên khớp và hiển thị cả những phòng ban CHƯA CÓ nhân viên nào (departments who have no match in employees table)."
    },
    "explanation_vi": "Toán tử `(+)` đặt ở cột `e.department_id(+)` nghĩa là bảng `employees` là bảng bị thiếu dữ liệu (phía thiếu). Điều này có nghĩa toàn bộ các phòng ban từ bảng `departments` đều được giữ lại, kể cả những phòng ban trống không có nhân viên nào (tương đương với RIGHT OUTER JOIN).",
    "key_takeaway_vi": "Dấu (+) đặt ở bảng nào thì bảng ĐỐI DIỆN sẽ được giữ lại toàn bộ (kể cả không có dữ liệu khớp).",
    "flashcard_front_vi": "Trong điều kiện e.dept_id(+) = d.dept_id, bảng nào được giữ lại toàn bộ dữ liệu?",
    "flashcard_back_vi": "Bảng departments (d). Đây tương đương với RIGHT OUTER JOIN."
}

DATA_MOD_7_9[146] = {
    "prompt_vi": "Loại kết nối nào sau đây KHÔNG CÓ SẴN (chưa được hỗ trợ) trong Oracle phiên bản 8i trở về trước?",
    "options_vi": {
        "A": "Full Outer Join",
        "B": "Self Join",
        "C": "Left Outer Join",
        "D": "Right Outer Join"
    },
    "explanation_vi": "Trong Oracle 8i trở về trước, Oracle chỉ có cú pháp `(+)` và luật của Oracle là dấu `(+)` không được phép xuất hiện ở cả hai vế của điều kiện (nghĩa là không thể làm Full Outer Join trực tiếp mà phải dùng phép UNION giữa Left Join và Right Join). Từ Oracle 9i hỗ trợ chuẩn SQL:1999 thì từ khóa `FULL OUTER JOIN` mới chính thức xuất hiện.",
    "key_takeaway_vi": "FULL OUTER JOIN chưa được hỗ trợ trực tiếp trong Oracle 8i trở về trước (mãi đến 9i mới có).",
    "flashcard_front_vi": "Tại sao Oracle 8i không thể viết a.id(+) = b.id(+)?",
    "flashcard_back_vi": "Vì cú pháp (+) của Oracle cấm đặt dấu (+) ở cả 2 vế. Muốn Full Join thời 8i phải dùng UNION giữa Left và Right Join."
}

DATA_MOD_7_9[147] = {
    "prompt_vi": "Phát biểu nào sau đây về việc sử dụng bí danh bảng (table aliases) và tiền tố bảng trong câu truy vấn Join là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Chúng ta có thể làm câu truy vấn ngắn gọn và dễ hiểu hơn bằng cách dùng bí danh bảng.",
        "B": "Tiền tố bảng bắt buộc phải dùng để phân biệt rõ ràng các cột có cùng tên ở các bảng khác nhau.",
        "C": "Chúng ta có thể cải thiện hiệu năng thực thi bằng cách dùng tiền tố bảng.",
        "D": "Tiền tố bảng bắt buộc phải sử dụng khi kết nối từ 3 bảng trở lên (must be used when joining more than three tables)."
    },
    "explanation_vi": "Phát biểu D là SAI vì không có quy định nào bắt buộc phải dùng tiền tố bảng khi nối từ 3 bảng trở lên. Tiền tố bảng chỉ bắt buộc khi các bảng có các cột trùng tên nhau (để tránh lỗi ambigous column).",
    "key_takeaway_vi": "Tiền tố bảng chỉ bắt buộc khi tên cột bị trùng lặp giữa các bảng; không bắt buộc dựa trên số lượng bảng.",
    "flashcard_front_vi": "Khi nào bắt buộc phải dùng tiền tố bảng (table_name.column)?",
    "flashcard_back_vi": "Khi câu truy vấn nối nhiều bảng mà có các cột trùng tên nhau (tránh lỗi ORA-00918: column ambiguously defined)."
}

DATA_MOD_7_9[148] = {
    "prompt_vi": "Câu lệnh nào sau đây thể hiện cách sử dụng ĐÚNG của phép kết nối tự nhiên (Natural Join)?",
    "options_vi": {
        "A": "SELECT department_id, department_name, location_id, city FROM departments d NATURAL JOIN locations l using (l.location_id);",
        "B": "SELECT department_id, department_name, location_id, city FROM departments NATURAL JOIN locations on (location_id);",
        "C": "SELECT department_id, department_name, location_id, city FROM departments NATURAL JOIN locations;",
        "D": "SELECT department_id, department_name, location_id, city FROM departments d NATURAL JOIN locations l WHERE d.location_id = l.location_id"
    },
    "explanation_vi": "`NATURAL JOIN` tự động tìm kiếm tất cả các cột có cùng tên và cùng kiểu dữ liệu ở cả hai bảng để làm điều kiện kết nối ngầm định. Vì vậy nó TUYỆT ĐỐI KHÔNG ĐI KÈM mệnh đề `ON` hoặc `USING`.",
    "key_takeaway_vi": "NATURAL JOIN tự động so khớp cột cùng tên, không được có mệnh đề ON hay USING.",
    "flashcard_front_vi": "Có được dùng mệnh đề ON hoặc USING trong câu lệnh NATURAL JOIN không?",
    "flashcard_back_vi": "KHÔNG. NATURAL JOIN tự động nối các cột cùng tên, dùng thêm ON/USING sẽ bị lỗi cú pháp."
}

DATA_MOD_7_9[149] = {
    "prompt_vi": "Phát biểu nào sau đây là KHÔNG ĐÚNG về các phép kết nối (joins)?",
    "options_vi": {
        "A": "Mệnh đề ON được sử dụng để chỉ định các điều kiện tùy ý hoặc chỉ định các cột để kết nối.",
        "B": "Phép kết nối Natural join và mệnh đề USING có thể được sử dụng cùng nhau (can be used together).",
        "C": "Sử dụng mệnh đề USING để chỉ định so khớp đúng một cột khi hai bảng có nhiều hơn một cột trùng tên.",
        "D": "Nếu các cột có cùng tên nhưng khác kiểu dữ liệu, Natural Join sẽ trả về lỗi."
    },
    "explanation_vi": "Phát biểu B là SAI vì `NATURAL JOIN` và mệnh đề `USING` là hai cơ chế loại trừ lẫn nhau (mutually exclusive). Nếu đã viết NATURAL JOIN thì không được viết USING, và ngược lại nếu dùng USING thì phải dùng cú pháp `JOIN ... USING (cột)`.",
    "key_takeaway_vi": "NATURAL JOIN và mệnh đề USING không bao giờ được dùng chung trong một câu lệnh.",
    "flashcard_front_vi": "Khi nào nên dùng mệnh đề USING thay vì NATURAL JOIN?",
    "flashcard_back_vi": "Khi 2 bảng có nhiều cột cùng tên nhưng ta chỉ muốn nối theo 1 cột duy nhất."
}

DATA_MOD_7_9[150] = {
    "prompt_vi": "Câu lệnh SQL nào sau đây hiển thị tên, tên phòng ban và thành phố của tất cả nhân viên có mức lương lớn hơn 10000?",
    "options_vi": {
        "A": "SELECT emp_name, department_name, city FROM employees e, departments d, locations l JOIN ON (e.department_id = d.department_id) AND (d.location_id = l.location_id) AND salary > 10000; (Theo đáp án đề CDAC)",
        "B": "SELECT emp_name, department_name, city FROM employees e, departments d, locations l WHERE salary > 10000;",
        "C": "SELECT emp_name, department_name, city FROM employees e JOIN departments d USING (department_id) JOIN locations l USING (location_id) WHERE salary > 10000;",
        "D": "SELECT emp_name, department_name, city FROM employees e NATURAL JOIN departments, locations WHERE salary > 10000;"
    },
    "explanation_vi": "Để kết nối 3 bảng `employees`, `departments`, `locations` và lọc nhân viên lương > 10000, câu lệnh cần liên kết khóa giữa employee với department (`department_id`) và department với location (`location_id`). (Lưu ý: Phương án C là chuẩn ANSI hoàn hảo, nhưng trong đề thi CDAC phương án A được đánh dấu 100 điểm).",
    "key_takeaway_vi": "Khi kết nối 3 bảng cần tối thiểu 2 điều kiện kết nối để tránh tích Descartes.",
    "flashcard_front_vi": "Để nối N bảng cần tối thiểu bao nhiêu điều kiện kết nối?",
    "flashcard_back_vi": "Tối thiểu N - 1 điều kiện kết nối."
}

DATA_MOD_7_9[151] = {
    "prompt_vi": "Bạn muốn lấy ra danh sách tất cả các nhân viên, bất kể họ đã được phân công vào phòng ban trong bảng departments hay chưa. Bạn dùng truy vấn nào?",
    "options_vi": {
        "A": "SELECT last_name, department_name FROM employees e LEFT OUTER JOIN departments d ON (e.department_id = d.department_id);",
        "B": "SELECT last_name, department_name FROM employees , departments(+);",
        "C": "SELECT last_name, department_name FROM employees JOIN departments (+);",
        "D": "SELECT last_name, department_name FROM employees e RIGHT OUTER JOIN departments d ON (e.department_id = d.department_id);"
    },
    "explanation_vi": "Vì bảng `employees` nằm ở phía bên trái của từ khóa JOIN và bạn muốn giữ lại TẤT CẢ các bản ghi của bảng employees (kể cả nhân viên chưa có phòng ban), bạn bắt buộc phải dùng `LEFT OUTER JOIN`.",
    "key_takeaway_vi": "Giữ lại toàn bộ dữ liệu bảng bên trái (dù không khớp với bảng phải) dùng LEFT OUTER JOIN.",
    "flashcard_front_vi": "Lấy tất cả nhân viên kể cả người chưa thuộc phòng ban nào dùng phép JOIN gì?",
    "flashcard_back_vi": "LEFT OUTER JOIN (với bảng employees đứng bên trái)."
}

DATA_MOD_7_9[152] = {
    "prompt_vi": "Điều nào sau đây là KHÔNG ĐÚNG về việc sử dụng các phép kết nối ngoài (outer joins)?",
    "options_vi": {
        "A": "Trong điều kiện WHERE, bạn dùng ký hiệu (+) theo sau tên cột của bảng thiếu dòng để thực hiện outer join.",
        "B": "Bạn dùng outer join để xem cả những dòng không thỏa mãn điều kiện kết nối thông thường.",
        "C": "Bạn không thể liên kết một điều kiện outer join với một điều kiện khác bằng toán tử OR.",
        "D": "Bạn không thể thực hiện phép nối ngoài khi kết nối nhiều hơn 2 bảng (You cannot an outer join while joining more than 2 tables)."
    },
    "explanation_vi": "Phát biểu D là SAI vì bạn hoàn toàn có thể thực hiện phép kết nối ngoài qua 3 bảng, 4 bảng hoặc nhiều hơn (ví dụ: A LEFT JOIN B ON ... LEFT JOIN C ON ...).",
    "key_takeaway_vi": "Outer join hoàn toàn có thể kết nối nhiều hơn 2 bảng.",
    "flashcard_front_vi": "Có thể thực hiện Outer Join trên 3 bảng trở lên không?",
    "flashcard_back_vi": "CÓ. Có thể kết hợp nhiều mệnh đề LEFT/RIGHT OUTER JOIN trên nhiều bảng liên tiếp."
}

DATA_MOD_7_9[153] = {
    "prompt_vi": "Phép kết nối nào sau đây còn được gọi là phép Inner Join (kết nối trong)?",
    "options_vi": {
        "A": "Self Join",
        "B": "Outer Join",
        "C": "Non-Equi Join",
        "D": "Equi Join (Phép kết nối bằng)"
    },
    "explanation_vi": "Phép `Equi Join` (kết nối dựa trên toán tử bằng `=`) là dạng phổ biến và tiêu biểu nhất của `Inner Join` (kết nối trong), trong đó chỉ những bản ghi thỏa mãn điều kiện bằng nhau ở cả hai bảng mới được trả về.",
    "key_takeaway_vi": "Equijoin (kết nối bằng) là dạng tiêu chuẩn của Inner Join.",
    "flashcard_front_vi": "Equijoin là gì?",
    "flashcard_back_vi": "Là phép kết nối trong sử dụng toán tử so sánh bằng (=) giữa các cột của 2 bảng."
}

DATA_MOD_7_9[154] = {
    "prompt_vi": "Điều gì là ĐÚNG khi kết nối các bảng thông qua một phép equijoin?",
    "options_vi": {
        "A": "Bạn chỉ định điều kiện equijoin trong mệnh đề SELECT hoặc FROM.",
        "B": "Bạn có thể kết nối n bảng (mỗi bảng có khóa chính 1 cột) bằng cách chỉ định tối thiểu là n-1 điều kiện kết nối.",
        "C": "Bạn chỉ có thể kết nối tối đa 2 cột qua một equijoin.",
        "D": "Bạn chỉ có thể kết nối tối đa 2 bảng qua một equijoin."
    },
    "explanation_vi": "Quy tắc kinh điển trong thiết kế truy vấn CSDL quan hệ: Để kết nối `n` bảng mà không bị tích Descartes, số điều kiện kết nối tối thiểu cần có luôn luôn là `n - 1` điều kiện.",
    "key_takeaway_vi": "Để kết nối n bảng cần tối thiểu n - 1 điều kiện kết nối.",
    "flashcard_front_vi": "Công thức tính số điều kiện kết nối tối thiểu để nối n bảng?",
    "flashcard_back_vi": "Số điều kiện tối thiểu = n - 1."
}

DATA_MOD_7_9[155] = {
    "prompt_vi": "Xét cấu trúc bảng EMPLOYEES, DEPARTMENTS và TAX (chứa MIN_SALARY, MAX_SALARY, TAX_PERCENT).\nTrong tình huống nào sau đây bạn sẽ sử dụng một truy vấn Non-Equijoin (kết nối không dùng dấu bằng)?",
    "options_vi": {
        "A": "Tìm số lượng nhân viên làm việc cho phòng Hành chính và có lương < 4000.",
        "B": "Tìm phần trăm thuế (tax percentage) áp dụng cho mỗi nhân viên (To find the tax percentage for each employee).",
        "C": "Liệt kê tên, chức vụ và tên người quản lý của tất cả nhân viên.",
        "D": "Tìm tên, lương và tên phòng ban của nhân viên không làm cùng với Smith."
    },
    "explanation_vi": "Để tìm mức thuế trong bảng `TAX`, tiền lương của nhân viên không thể so sánh bằng (`=`) với mức thuế cụ thể, mà phải so sánh trong khoảng: `WHERE e.salary BETWEEN t.min_salary AND t.max_salary`. Phép kết nối dùng toán tử `BETWEEN ... AND` hoặc `>=`, `<=` chính là định nghĩa chuẩn của `Non-Equijoin`.",
    "key_takeaway_vi": "So sánh giá trị nằm trong khoảng (dùng BETWEEN ... AND hoặc >=, <=) là Non-Equijoin.",
    "flashcard_front_vi": "Non-Equijoin là gì? Cho ví dụ thực tế.",
    "flashcard_back_vi": "Là phép nối dùng toán tử khác dấu bằng (như BETWEEN, >=, <=). Ví dụ: Tra cứu bậc lương hoặc khung thuế thu nhập."
}

DATA_MOD_7_9[156] = {
    "prompt_vi": "Để tạo ra một tập kết quả có ý nghĩa mà không bị tích Descartes, số lượng điều kiện tối thiểu phải xuất hiện trong mệnh đề WHERE của một câu truy vấn nối 4 bảng là bao nhiêu?",
    "options_vi": {
        "A": "2",
        "B": "4",
        "C": "3",
        "D": "8"
    },
    "explanation_vi": "Áp dụng công thức `n - 1`: Với `n = 4` bảng, số điều kiện kết nối tối thiểu cần thiết trong mệnh đề WHERE là `4 - 1 = 3` điều kiện.",
    "key_takeaway_vi": "Nối 4 bảng cần tối thiểu: 4 - 1 = 3 điều kiện kết nối.",
    "flashcard_front_vi": "Nối 4 bảng cần tối thiểu bao nhiêu điều kiện WHERE để không bị Cartesian Product?",
    "flashcard_back_vi": "3 điều kiện kết nối."
}

DATA_MOD_7_9[157] = {
    "prompt_vi": "Trong trường hợp nào sau đây bạn sẽ sử dụng phép kết nối ngoài (Outer Join)?",
    "options_vi": {
        "A": "Các bảng được kết nối có các cột mang ràng buộc NOT NULL.",
        "B": "Các bảng được kết nối có cả dữ liệu khớp và dữ liệu không khớp mà bạn vẫn muốn hiển thị (both matched and unmatched data).",
        "C": "Các bảng được kết nối chỉ có dữ liệu không khớp.",
        "D": "Các bảng được kết nối chỉ có dữ liệu khớp."
    },
    "explanation_vi": "Phép kết nối trong (Inner Join) chỉ hiển thị các dòng có dữ liệu khớp ở cả hai bảng. Khi bạn muốn hiển thị các dòng khớp VÀ CẢ các dòng không khớp từ một hoặc hai bảng (ví dụ: phòng ban chưa có nhân viên nào, khách hàng chưa mua đơn nào), bạn bắt buộc phải dùng `Outer Join`.",
    "key_takeaway_vi": "Outer Join dùng khi muốn lấy cả dữ liệu khớp lẫn các bản ghi không có đối chiếu ở bảng kia.",
    "flashcard_front_vi": "Mục đích chính của Outer Join là gì?",
    "flashcard_back_vi": "Hiển thị cả các bản ghi không có giá trị khớp ở bảng liên kết (tránh bị mất dữ liệu như Inner Join)."
}

DATA_MOD_7_9[158] = {
    "prompt_vi": "Tích Descartes (Cartesian product) xảy ra khi nào trong câu truy vấn Join?",
    "options_vi": {
        "A": "Tất cả các dòng của bảng thứ nhất được ghép với tất cả các dòng của bảng thứ hai.",
        "B": "Điều kiện kết nối bị bỏ sót (A join condition is omitted).",
        "C": "Điều kiện kết nối không hợp lệ (A join condition is invalid).",
        "D": "Hai bảng được kết nối trên các cột có tên khác nhau (Theo đáp án trắc nghiệm đề gốc CDAC đánh dấu 100)"
    },
    "explanation_vi": "⚠️ LƯU Ý GIẢNG VIÊN & ĐỀ THI: Về mặt lý thuyết chuẩn CSDL quan hệ: Tích Descartes xảy ra khi 'Điều kiện kết nối bị bỏ quên' (phương án B) hoặc 'Điều kiện kết nối không hợp lệ' (phương án C), dẫn đến kết quả là phương án A. Tuy nhiên trong file bài tập gốc của CDAC, đáp án chấm phương án D. Sinh viên khi làm bài kiểm tra trắc nghiệm CDAC cần ghi nhớ đáp án D của ngân hàng đề, nhưng khi đi làm thực tế cần nắm rõ bản chất: Tích Descartes xuất hiện khi thiếu điều kiện kết nối!",
    "key_takeaway_vi": "Lý thuyết chuẩn: Tích Descartes xảy ra khi quên điều kiện kết nối. Đề thi CDAC chọn phương án D.",
    "flashcard_front_vi": "Lý do chính khiến câu lệnh SQL sinh ra Cartesian Product?",
    "flashcard_back_vi": "Do quên viết điều kiện kết nối trong mệnh đề WHERE hoặc ON. (Lưu ý đáp án bài thi CDAC đánh dấu D)."
}

DATA_MOD_7_9[159] = {
    "prompt_vi": "Loại kết nối nào sau đây KHÔNG PHẢI là một loại kết nối (Join) hợp lệ trong SQL?",
    "options_vi": {
        "A": "External Join",
        "B": "Outer Join",
        "C": "Inner Join",
        "D": "Natural join"
    },
    "explanation_vi": "Trong chuẩn SQL chỉ có các loại: Inner Join, Outer Join (Left, Right, Full), Natural Join, Cross Join. Thuật ngữ 'External Join' là từ bịa đặt, hoàn toàn không tồn tại trong tài liệu chuẩn.",
    "key_takeaway_vi": "Không có loại kết nối nào tên là 'External Join'.",
    "flashcard_front_vi": "Trong SQL có khái niệm 'External Join' không?",
    "flashcard_back_vi": "KHÔNG. Chỉ có Inner Join, Outer Join, Cross Join, Natural Join."
}

DATA_MOD_7_9[160] = {
    "prompt_vi": "Loại kết nối nào được sử dụng trong câu truy vấn sau?\nSELECT e.employee_id, e.last_name, d.department_id, d.location_id\nFROM employees e, departments d\nWHERE e.department_id = d.department_id;",
    "options_vi": {
        "A": "Self Join",
        "B": "Non-equi Join",
        "C": "Equi join (Kết nối bằng)",
        "D": "Left Outer join"
    },
    "explanation_vi": "Điều kiện kết nối sử dụng toán tử dấu bằng: `WHERE e.department_id = d.department_id`. Đây là định nghĩa chính xác của phép `Equi join`.",
    "key_takeaway_vi": "Kết nối dựa trên dấu bằng (=) giữa 2 cột là Equi join.",
    "flashcard_front_vi": "Phép kết nối nào dùng dấu '=' giữa các cột?",
    "flashcard_back_vi": "Equi join."
}

# MODULE 9: Sub Queries (Q161 - Q180)
DATA_MOD_7_9[161] = {
    "prompt_vi": "Đánh giá câu lệnh:\nSELECT employee_id, name FROM employee WHERE employee_id NOT IN (SELECT employee_id FROM employee WHERE department_id = 30 AND job = 'CLERK');\nĐiều gì sẽ xảy ra nếu câu truy vấn con (inner query) trả về ít nhất một giá trị NULL?",
    "options_vi": {
        "A": "Sẽ báo lỗi cú pháp.",
        "B": "Chỉ các dòng có employee_id bằng NULL mới được chọn.",
        "C": "Tất cả các dòng trong bảng employee đều sẽ được hiển thị.",
        "D": "KHÔNG CÓ DÒNG NÀO được chọn từ bảng EMPLOYEE (No rows would be selected)."
    },
    "explanation_vi": "🔥 BẪY KINH ĐIỂN NHẤT CỦA TOÁN TỬ NOT IN: Trong logic 3 giá trị của SQL (TRUE, FALSE, UNKNOWN), biểu thức `x NOT IN (val1, val2, NULL)` tương đương với `x != val1 AND x != val2 AND x != NULL`. Vì `x != NULL` luôn trả về `UNKNOWN`, nên toàn bộ mệnh đề AND sẽ không bao giờ có kết quả TRUE! Kết quả là câu truy vấn ngoài hoàn toàn rỗng (0 dòng được trả về)!",
    "key_takeaway_vi": "Nếu tập kết quả của subquery chứa NULL, toán tử NOT IN sẽ luôn trả về rỗng (0 dòng).",
    "flashcard_front_vi": "Hậu quả khi subquery trong toán tử NOT IN trả về có chứa giá trị NULL?",
    "flashcard_back_vi": "Câu truy vấn ngoài sẽ trả về RỖNG (0 dòng) do điều kiện so sánh với NULL trả về UNKNOWN."
}

DATA_MOD_7_9[162] = {
    "prompt_vi": "Mệnh đề nào sau đây KHÔNG THỂ sử dụng câu truy vấn con (subquery)?",
    "options_vi": {
        "A": "Trong mệnh đề FROM của câu lệnh SELECT.",
        "B": "Trong mệnh đề GROUP BY của câu lệnh SELECT (in the GROUP BY clause).",
        "C": "Trong mệnh đề SET của câu lệnh UPDATE.",
        "D": "Trong mệnh đề WHERE của câu lệnh SELECT."
    },
    "explanation_vi": "SQL cho phép sử dụng Subquery trong: `WHERE`, `HAVING`, `FROM` (inline view), `SELECT` (scalar subquery), và `SET` của UPDATE. Tuy nhiên, mệnh đề `GROUP BY` TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP chứa subquery.",
    "key_takeaway_vi": "Subquery không bao giờ được đặt trong mệnh đề GROUP BY.",
    "flashcard_front_vi": "Mệnh đề nào trong SELECT không bao giờ được phép chứa Subquery?",
    "flashcard_back_vi": "Mệnh đề GROUP BY."
}

DATA_MOD_7_9[163] = {
    "prompt_vi": "Phát biểu nào sau đây mô tả đúng nhất về một Khung nhìn nội tuyến (Inline View)?",
    "options_vi": {
        "A": "Một câu truy vấn con (subquery) nằm trong mệnh đề FROM của một câu truy vấn khác.",
        "B": "Một subquery có thể chứa mệnh đề ORDER BY.",
        "C": "Một tên gọi khác của view có chứa các hàm nhóm.",
        "D": "Một đối tượng lược đồ (schema object) được lưu vĩnh viễn trong CSDL."
    },
    "explanation_vi": "`Inline View` là thuật ngữ trong Oracle SQL chỉ một câu truy vấn con được đặt trực tiếp trong mệnh đề `FROM` của câu truy vấn cha: `SELECT ... FROM (SELECT ... FROM ...) alias`. Nó chỉ tồn tại trong suốt quá trình thực thi câu truy vấn đó và không phải là đối tượng lưu trong từ điển dữ liệu.",
    "key_takeaway_vi": "Inline View là một subquery nằm trong mệnh đề FROM của câu truy vấn khác.",
    "flashcard_front_vi": "Inline View là gì?",
    "flashcard_back_vi": "Là câu truy vấn con (Subquery) được đặt ngay trong mệnh đề FROM đóng vai trò như một bảng tạm."
}

DATA_MOD_7_9[164] = {
    "prompt_vi": "Phát biểu nào sau đây về các câu truy vấn con (subqueries) là ĐÚNG?",
    "options_vi": {
        "A": "Một câu truy vấn con có thể trả về từ 0 dòng trở lên (zero or more rows).",
        "B": "Một câu truy vấn con chỉ được phép trả về duy nhất 1 dòng.",
        "C": "Truy vấn con không thể lồng quá 2 cấp độ.",
        "D": "Truy vấn con chỉ có thể dùng duy nhất trong câu lệnh SELECT."
    },
    "explanation_vi": "Một subquery có thể trả về: 0 dòng (không có kết quả), 1 dòng (Single-row subquery), hoặc nhiều dòng (Multiple-row subquery). Subquery cũng có thể dùng trong INSERT, UPDATE, DELETE và có thể lồng nhiều cấp.",
    "key_takeaway_vi": "Subquery có thể trả về 0, 1 hoặc nhiều dòng tùy thuộc vào dữ liệu.",
    "flashcard_front_vi": "Một subquery có thể trả về bao nhiêu dòng?",
    "flashcard_back_vi": "Có thể trả về 0 dòng, 1 dòng (single-row) hoặc nhiều dòng (multi-row)."
}

DATA_MOD_7_9[165] = {
    "prompt_vi": "Câu lệnh nào sau đây hiển thị các nhân viên có cùng chức vụ (job_id) với nhân viên có họ là 'Haas' và có mức lương lớn hơn 10000?",
    "options_vi": {
        "A": "SELECT last_name, job_id FROM employees WHERE job_id IN (SELECT job_id FROM employees WHERE last_name = 'Haas') AND salary > 10000;",
        "B": "SELECT last_name, job_id FROM employees WHERE last_name = 'Haas' AND salary >10000",
        "C": "SELECT last_name, job_id FROM employees WHERE job_id IN (SELECT job_id FROM employees WHERE Salary > 10000) AND last_name = 'Haas'",
        "D": "SELECT last_name, job_id FROM employees WHERE job_id = (SELECT job_id FROM employees WHERE last_name = 'Haas' AND salary > 10000);"
    },
    "explanation_vi": "Để tìm chức vụ của 'Haas', ta dùng subquery: `SELECT job_id FROM employees WHERE last_name = 'Haas'`. Vì có thể có nhiều người họ Haas, dùng toán tử `IN` là an toàn nhất. Điều kiện lương > 10000 phải đặt ở câu truy vấn ngoài để lọc nhân viên thỏa mãn.",
    "key_takeaway_vi": "Tìm dữ liệu dựa trên kết quả người khác cần dùng Subquery kết hợp toán tử IN hoặc =.",
    "flashcard_front_vi": "Tại sao nên dùng toán tử IN thay vì '=' khi so sánh với subquery tìm theo tên?",
    "flashcard_back_vi": "Vì có thể có nhiều nhân viên trùng tên, khi đó subquery trả về nhiều dòng khiến toán tử '=' bị lỗi ORA-01427."
}

DATA_MOD_7_9[166] = {
    "prompt_vi": "__________ được sử dụng để lấy dữ liệu từ một hoặc nhiều bảng khi không có mối quan hệ (foreign key) trực tiếp giữa các bảng?",
    "options_vi": {
        "A": "Truy vấn con (Sub query)",
        "B": "Cả hai (Both)",
        "C": "Phép kết nối (Joins)",
        "D": "Không câu nào ở trên"
    },
    "explanation_vi": "Khi hai bảng không có mối quan hệ khóa ngoại trực tiếp để JOIN, hoặc dữ liệu cần lọc dựa trên một tập tiêu chí trung gian, `Subquery` là công cụ mạnh mẽ nhất để trích xuất dữ liệu mà không cần phải thực hiện phép kết nối bảng phức tạp.",
    "key_takeaway_vi": "Subquery cho phép truy xuất dữ liệu giữa các bảng không có quan hệ khóa trực tiếp.",
    "flashcard_front_vi": "Công cụ nào hiệu quả để lấy dữ liệu khi 2 bảng không có quan hệ trực tiếp?",
    "flashcard_back_vi": "Subquery (truy vấn con)."
}

DATA_MOD_7_9[167] = {
    "prompt_vi": "Một câu truy vấn con (subquery) có thể được sử dụng để làm gì?",
    "options_vi": {
        "A": "Lấy dữ liệu dựa trên một điều kiện chưa biết trước (Retrieve data based on an unknown condition).",
        "B": "Tạo các nhóm dữ liệu.",
        "C": "Chuyển đổi dữ liệu sang định dạng khác.",
        "D": "Sắp xếp dữ liệu theo thứ tự cụ thể."
    },
    "explanation_vi": "Mục đích kinh điển nhất của Subquery là giải quyết bài toán phụ thuộc vào một giá trị chưa biết trước. Ví dụ: 'Ai có lương cao hơn lương của Abel?' -> Lương của Abel là ẩn số chưa biết trước, cần 1 subquery để tìm trước khi lọc câu chính.",
    "key_takeaway_vi": "Subquery giải quyết bài toán lọc dữ liệu dựa trên giá trị chưa biết trước.",
    "flashcard_front_vi": "Ứng dụng điển hình nhất của Subquery là gì?",
    "flashcard_back_vi": "Tìm kiếm dữ liệu dựa trên một giá trị ẩn/chưa biết trước (ví dụ: lương lớn hơn lương trung bình)."
}

DATA_MOD_7_9[168] = {
    "prompt_vi": "Xem dữ liệu bảng EMPLOYEES: Getz (phòng 10, lương 3000), Davis (20, 1500), King (20, 2200), Davis (30, 5000).\nTruy vấn con nào sau đây SẼ KHÔNG HOẠT ĐỘNG (báo lỗi)?",
    "options_vi": {
        "A": "SELECT distinct department_id FROM employees Where salary > ANY (SELECT AVG(salary) FROM employees GROUP BY department_id)",
        "B": "SELECT last_name FROM employees Where salary > ANY (SELECT MAX(salary) FROM employees GROUP BY department_id)",
        "C": "SELECT * FROM employees where salary > (SELECT MIN(salary) FROM employees GROUP BY department_id)",
        "D": "SELECT department_id FROM employees WHERE SALARY > ALL (SELECT AVG(salary) FROM employees GROUP BY department_id)"
    },
    "explanation_vi": "Trong câu C, subquery `SELECT MIN(salary) ... GROUP BY department_id` trả về NHIỀU DÒNG (mỗi phòng ban 1 mức lương min). Nhưng ở câu lệnh cha lại dùng toán tử so sánh đơn dòng `>`. Việc dùng toán tử đơn dòng với subquery trả về nhiều dòng sẽ gây ra lỗi nghiêm trọng: `ORA-01427: single-row subquery returns more than one row`!",
    "key_takeaway_vi": "Toán tử so sánh đơn dòng (> , <, =) sẽ báo lỗi ORA-01427 nếu subquery trả về nhiều hơn 1 dòng.",
    "flashcard_front_vi": "Lỗi 'single-row subquery returns more than one row' (ORA-01427) xảy ra khi nào?",
    "flashcard_back_vi": "Khi dùng toán tử so sánh đơn dòng (=, >, <) mà subquery lại trả về danh sách nhiều dòng."
}

DATA_MOD_7_9[169] = {
    "prompt_vi": "Công dụng của cột giả LEVEL (LEVEL pseudocolumn) trong Oracle là gì?",
    "options_vi": {
        "A": "Chỉ định node bắt đầu của truy vấn phân cấp.",
        "B": "Dùng để hiển thị cấp độ (độ sâu) của một dòng trong cây phân cấp (display level in hierarchy).",
        "C": "Không câu nào đúng.",
        "D": "Dùng để san bằng kết quả truy vấn."
    },
    "explanation_vi": "Trong truy vấn phân cấp hình cây của Oracle (`Hierarchical Query`: CONNECT BY ... START WITH), `LEVEL` là cột giả trả về số nguyên từ 1 trở đi, đại diện cho độ sâu của node hiện tại trong cấu trúc phả hệ (gốc là 1, con trực tiếp là 2, cháu là 3...).",
    "key_takeaway_vi": "Cột giả LEVEL trả về độ sâu của nút trong truy vấn phân cấp hình cây.",
    "flashcard_front_vi": "Cột giả LEVEL dùng trong loại truy vấn nào của Oracle?",
    "flashcard_back_vi": "Dùng trong truy vấn phân cấp hình cây (Hierarchical Queries với CONNECT BY)."
}

DATA_MOD_7_9[170] = {
    "prompt_vi": "Câu truy vấn nào sau đây sẽ hiển thị chi tiết nhân viên và người quản lý của họ theo cấu trúc cây TỪ TRÊN XUỐNG (TOP-DOWN tree structure), bắt đầu từ nhân viên 'King'?",
    "options_vi": {
        "A": "SELECT employee_id, last_name, job_id, manager_id FROM employees START WITH last_name = 'King' CONNECT BY PRIOR employee_id = manager_id ;",
        "B": "SELECT employee_id, last_name, job_id, manager_id FROM employees START WITH last_name = 'King' CONNECT BY PRIOR manager_id = employee_id;",
        "C": "SELECT employee_id, last_name, job_id, manager_id FROM employees START WITH last_name = 'King' CONNECT BY PRIOR employee_id TOP_DOWN;",
        "D": "SELECT employee_id, last_name, job_id, manager_id FROM employees START WITH last_name = 'King' CONNECT BY TOP_DOWN employee_id = manager_id ;"
    },
    "explanation_vi": "Để duyệt cây từ trên xuống dưới (từ sếp xuống nhân viên cấp dưới): Node cha phải là người đi trước (`PRIOR`), tức là ID của người quản lý cấp trước phải bằng ID sếp của cấp sau: `CONNECT BY PRIOR employee_id = manager_id`. Điểm bắt đầu duyệt gốc cây chỉ định bởi `START WITH last_name = 'King'`.",
    "key_takeaway_vi": "Duyệt cây từ trên xuống: CONNECT BY PRIOR parent_id = child_id (PRIOR employee_id = manager_id).",
    "flashcard_front_vi": "Cú pháp duyệt cây từ trên xuống (Top-down) trong Oracle?",
    "flashcard_back_vi": "START WITH gốc CONNECT BY PRIOR id_cha = id_con."
}

DATA_MOD_7_9[171] = {
    "prompt_vi": "Kết quả của câu truy vấn sau sẽ là gì?\nSELECT last_name, job_id, salary FROM employees\nWHERE job_id = (SELECT job_id FROM employees WHERE employee_id = 141)\nAND salary > (SELECT salary FROM employees WHERE employee_id = 143);",
    "options_vi": {
        "A": "Hiển thị nhân viên có cùng chức vụ với 141 hoặc 143 và lương cao hơn 141 hoặc 143.",
        "B": "Hiển thị nhân viên có cùng chức vụ với cả 141 và 143 và lương cao hơn cả hai.",
        "C": "Hiển thị nhân viên có cùng chức vụ với 141 hoặc có mức lương lớn hơn nhân viên 143.",
        "D": "Hiển thị các nhân viên có cùng chức vụ với nhân viên 141 VÀ có mức lương lớn hơn nhân viên 143."
    },
    "explanation_vi": "Phân tích 2 điều kiện nối bằng `AND`: 1. `job_id = (SELECT ... WHERE employee_id = 141)` -> chức vụ giống nhân viên 141. 2. `salary > (SELECT ... WHERE employee_id = 143)` -> lương lớn hơn lương nhân viên 143. Cả hai điều kiện bắt buộc phải đồng thời thỏa mãn.",
    "key_takeaway_vi": "Toán tử AND đòi hỏi đồng thời cả 2 điều kiện: cùng job_id với 141 VÀ lương > 143.",
    "flashcard_front_vi": "Giải thích ý nghĩa logic của toán tử AND giữa 2 subquery so sánh?",
    "flashcard_back_vi": "Bản ghi chỉ được chọn khi thỏa mãn đồng thời cả hai điều kiện của 2 subquery."
}

DATA_MOD_7_9[172] = {
    "prompt_vi": "Phát biểu nào sau đây về các câu truy vấn con (subqueries) là ĐÚNG?",
    "options_vi": {
        "A": "Truy vấn con KHÔNG THỂ tham chiếu đến bảng không có trong mệnh đề FROM của truy vấn ngoài.",
        "B": "Truy vấn con bắt buộc phải đặt ở bên tay phải của toán tử so sánh.",
        "C": "Truy vấn con có thể trả về nhiều cột (Subqueries can return multiple columns).",
        "D": "Truy vấn con không thể lồng quá 3 cấp độ."
    },
    "explanation_vi": "Truy vấn con hoàn toàn có thể trả về nhiều cột (Multiple-column subquery), ví dụ trong so sánh cặp: `WHERE (dept_id, manager_id) IN (SELECT dept_id, manager_id FROM ...)`. (Trong Oracle, subquery có thể lồng tới 255 cấp, và có thể đặt bên trái hoặc phải toán tử so sánh).",
    "key_takeaway_vi": "Subquery có thể trả về nhiều cột (Multiple-column subquery) để so sánh nhiều thuộc tính cùng lúc.",
    "flashcard_front_vi": "Subquery có thể trả về nhiều cột không?",
    "flashcard_back_vi": "CÓ. Gọi là Multiple-column subquery (truy vấn con nhiều cột)."
}

DATA_MOD_7_9[173] = {
    "prompt_vi": "Toán tử nào sau đây KHÔNG PHẢI là một toán tử so sánh nhiều dòng (multiple-row comparison operator)?",
    "options_vi": {
        "A": "ANY",
        "B": "IN",
        "C": "EACH",
        "D": "ALL"
    },
    "explanation_vi": "Bộ 3 toán tử so sánh nhiều dòng chuẩn trong SQL là: `IN`, `ANY` (hoặc `SOME`), và `ALL`. Hoàn toàn không có toán tử nào tên là `EACH` trong ngôn ngữ SQL.",
    "key_takeaway_vi": "Toán tử so sánh nhiều dòng gồm: IN, ANY, ALL. Không có toán tử EACH.",
    "flashcard_front_vi": "Kể tên các toán tử so sánh nhiều dòng (Multiple-row operators) trong SQL?",
    "flashcard_back_vi": "IN, ANY (hoặc SOME), ALL."
}

DATA_MOD_7_9[174] = {
    "prompt_vi": "Đánh giá câu lệnh SQL:\nSELECT product_id, product_name, price FROM product\nWHERE supplier_id IN (SELECT supplier_id FROM product WHERE price > 120 OR qty_in_stock > 100);\nNhững giá trị nào sẽ được hiển thị?",
    "options_vi": {
        "A": "Mã, tên, giá của các sản phẩm có giá > 120$ hoặc tồn kho > 100.",
        "B": "Mã, tên, giá của các sản phẩm có giá > 120$ và tồn kho > 100.",
        "C": "Mã, tên, giá của tất cả sản phẩm được cung cấp bởi nhà cung cấp có ít nhất một sản phẩm giá > 120$ hoặc tồn kho > 100.",
        "D": "Mã, tên, giá của các sản phẩm có giá > 120$ hoặc tồn kho < 100."
    },
    "explanation_vi": "Truy vấn con tìm danh sách các `supplier_id` của những nhà cung cấp có sản phẩm giá > 120 hoặc tồn kho > 100. Sau đó câu truy vấn ngoài lấy ra TẤT CẢ các sản phẩm của các nhà cung cấp này (kể cả những sản phẩm giá thấp hơn 120). Do đó phương án C là cách diễn đạt chính xác nhất.",
    "key_takeaway_vi": "Mệnh đề WHERE supplier_id IN (...) lọc theo nhà cung cấp thỏa mãn, trả về toàn bộ sản phẩm của các NCC đó.",
    "flashcard_front_vi": "Tại sao câu lệnh này không chỉ trả về các sản phẩm giá > 120?",
    "flashcard_back_vi": "Vì điều kiện WHERE ngoài lọc theo supplier_id, nên mọi sản phẩm của nhà cung cấp đó đều được lấy."
}

DATA_MOD_7_9[175] = {
    "prompt_vi": "Một câu truy vấn con (subquery) có thể được sử dụng để làm gì?",
    "options_vi": {
        "A": "Sắp xếp dữ liệu theo thứ tự cụ thể.",
        "B": "Tạo các nhóm dữ liệu.",
        "C": "Truy xuất dữ liệu dựa trên một điều kiện chưa biết trước (Retrieve data based on an unknown condition).",
        "D": "Chuyển đổi dữ liệu sang định dạng khác."
    },
    "explanation_vi": "Subquery được dùng phổ biến nhất để cung cấp giá trị cho mệnh đề WHERE/HAVING khi điều kiện lọc cần tính toán động tại thời điểm chạy (giá trị chưa biết trước).",
    "key_takeaway_vi": "Subquery dùng để lấy dữ liệu dựa trên các điều kiện lọc động chưa biết trước.",
    "flashcard_front_vi": "Ứng dụng chính của subquery trong điều kiện lọc?",
    "flashcard_back_vi": "Tính toán động giá trị so sánh tại thời điểm chạy truy vấn."
}

DATA_MOD_7_9[176] = {
    "prompt_vi": "Phát biểu nào sau đây về các câu truy vấn con là KHÔNG ĐÚNG?",
    "options_vi": {
        "A": "Một câu truy vấn con đơn dòng chỉ có thể lấy được duy nhất một cột và một dòng (only one column and one row).",
        "B": "Một câu truy vấn con nhiều dòng có thể lấy nhiều dòng và nhiều cột.",
        "C": "Một truy vấn con nhiều dòng có thể được so sánh bằng cách dùng toán tử \">\" đi kèm với ANY hoặc ALL.",
        "D": "Một câu truy vấn con đơn dòng có thể trả về duy nhất một dòng nhưng có nhiều cột."
    },
    "explanation_vi": "Phát biểu A là SAI vì một truy vấn con đơn dòng (Single-row subquery) hoàn toàn có thể trả về MỘT DÒNG VÀ NHIỀU CỘT khi dùng trong so sánh cặp (Pairwise comparison): `WHERE (col1, col2) = (SELECT a, b FROM table WHERE id = 1)`.",
    "key_takeaway_vi": "Single-row subquery có thể trả về nhiều cột nếu dùng trong phép so sánh nhiều cột (col1, col2) = (...).",
    "flashcard_front_vi": "Single-row subquery có bắt buộc chỉ được chứa 1 cột không?",
    "flashcard_back_vi": "KHÔNG. Nó có thể trả về 1 dòng gồm nhiều cột trong so sánh đa thuộc tính: (col1, col2) = (SELECT c1, c2...)."
}

DATA_MOD_7_9[177] = {
    "prompt_vi": "Bạn định nghĩa một truy vấn con nhiều dòng trong mệnh đề WHERE với toán tử so sánh bằng \"=\". Điều gì xảy ra khi câu truy vấn chính được thực thi?",
    "options_vi": {
        "A": "Câu truy vấn chính bị lỗi vì truy vấn con nhiều dòng không thể dùng trực tiếp với toán tử so sánh đơn dòng \"=\".",
        "B": "Câu truy vấn chính thực thi với giá trị cuối cùng được trả về bởi truy vấn con.",
        "C": "Câu truy vấn chính thực thi với tất cả các giá trị được trả về.",
        "D": "Câu truy vấn chính thực thi với giá trị đầu tiên được trả về."
    },
    "explanation_vi": "Toán tử `=` là toán tử so sánh đơn dòng (Single-row comparison operator). Nếu subquery trả về nhiều hơn một dòng, Oracle sẽ báo lỗi ngay lập tức: `ORA-01427: single-row subquery returns more than one row`. Muốn so sánh với nhiều dòng phải dùng toán tử `IN` hoặc `= ANY`.",
    "key_takeaway_vi": "Toán tử '=' đi kèm subquery nhiều dòng sẽ gây lỗi ORA-01427.",
    "flashcard_front_vi": "Tại sao không thể dùng toán tử '=' với subquery trả về nhiều dòng?",
    "flashcard_back_vi": "Báo lỗi ORA-01427. Phải thay '=' bằng toán tử IN hoặc = ANY."
}

DATA_MOD_7_9[178] = {
    "prompt_vi": "Toán tử nào sau đây có thể được sử dụng với một câu truy vấn con trả về nhiều dòng (multiple-row subquery)?",
    "options_vi": {
        "A": "LIKE",
        "B": "=",
        "C": "NOT IN",
        "D": "BETWEEN"
    },
    "explanation_vi": "Toán tử `NOT IN` (cùng với `IN`, `ANY`, `ALL`) là các toán tử hợp lệ chuyên dùng để so sánh với tập hợp nhiều dòng trả về từ subquery. Các toán tử LIKE, =, BETWEEN là toán tử đơn dòng.",
    "key_takeaway_vi": "Toán tử so sánh đa dòng gồm: IN, NOT IN, ANY, ALL.",
    "flashcard_front_vi": "Toán tử nào so sánh được với tập hợp kết quả nhiều dòng?",
    "flashcard_back_vi": "NOT IN, IN, ANY, ALL."
}

DATA_MOD_7_9[179] = {
    "prompt_vi": "Phát biểu nào sau đây về truy vấn con là ĐÚNG?",
    "options_vi": {
        "A": "Truy vấn con đơn dòng chỉ có thể lấy dữ liệu từ một bảng duy nhất.",
        "B": "Truy vấn con đơn dòng không thể dùng trong điều kiện có toán tử LIKE.",
        "C": "Một câu lệnh truy vấn SQL không thể hiển thị trực tiếp dữ liệu từ bảng B nếu bảng B chỉ được tham chiếu bên trong subquery (cannot display data from table B).",
        "D": "Câu lệnh SQL có thể hiển thị dữ liệu từ bảng B nằm trong subquery mà không cần bảng B ở mệnh đề FROM ngoài."
    },
    "explanation_vi": "Mệnh đề `SELECT` của truy vấn ngoài chỉ có thể chiếu các cột thuộc các bảng được liệt kê trong mệnh đề `FROM` của chính nó. Các cột của bảng chỉ xuất hiện trong subquery thì không thể được hiển thị trực tiếp ở danh sách cột của truy vấn cha.",
    "key_takeaway_vi": "Cột nằm trong Subquery không thể xuất hiện trong danh sách SELECT của truy vấn ngoài.",
    "flashcard_front_vi": "Có thể SELECT các cột của bảng chỉ nằm trong Subquery ra ngoài không?",
    "flashcard_back_vi": "KHÔNG. Mệnh đề SELECT ngoài chỉ được lấy cột từ các bảng có trong mệnh đề FROM ngoài."
}

DATA_MOD_7_9[180] = {
    "prompt_vi": "Xét cấu trúc bảng EMPLOYEES và NEW_EMPLOYEES. Câu lệnh DELETE nào sau đây là hợp lệ?",
    "options_vi": {
        "A": "DELETE FROM employees WHERE employee_id IN (SELECT employee_id FROM new_employees WHERE name = 'Carrey');",
        "B": "DELETE FROM employees WHERE employee_id = (SELECT employee_id FROM employees);",
        "C": "DELETE * FROM employees WHERE employee_id IN (SELECT employee_id FROM new_employees WHERE last_name = 'Carrey');",
        "D": "DELETE * FROM employees WHERE employee_id = (SELECT employee_id FROM new_employees);"
    },
    "explanation_vi": "Phương án A là câu lệnh DELETE chuẩn: `DELETE FROM employees WHERE employee_id IN (SELECT ...)`. Các phương án C và D sai cú pháp vì có dấu sao `DELETE *`; phương án B sai vì subquery trả về nhiều dòng nhưng lại dùng dấu bằng `=`.",
    "key_takeaway_vi": "DELETE dùng subquery nhiều dòng phải kết hợp với toán tử IN và không bao giờ có dấu *.",
    "flashcard_front_vi": "Cú pháp DELETE có điều kiện subquery nhiều dòng đúng?",
    "flashcard_back_vi": "DELETE FROM table WHERE id IN (SELECT id FROM ...);"
}

print(f"Loaded {len(DATA_MOD_7_9)} questions for Modules 7-9.")
