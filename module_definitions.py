# -*- coding: utf-8 -*-
"""
Helper library for database domain translations and explanations
Curated by Database Lecturer & Senior DB Engineer
"""

MODULE_INFO = {
    1: {
        "title_vi": "Module 1: Tổng quan về DBMS & Kiến trúc Oracle",
        "description_vi": "Kiến trúc hệ quản trị cơ sở dữ liệu, Oracle Instance, SGA, PGA, Background Processes (LGWR, DBWn, CKPT), tính chất ACID và các mức trừu tượng dữ liệu."
    },
    2: {
        "title_vi": "Module 2: Giới thiệu về SQL & Mệnh đề SELECT",
        "description_vi": "Cú pháp cơ bản của SQL, biểu thức số học, đặt bí danh cho cột (Column Alias), xử lý giá trị NULL, từ khóa DISTINCT và thứ tự ưu tiên các toán tử."
    },
    3: {
        "title_vi": "Module 3: Ngôn ngữ định nghĩa dữ liệu (DDL)",
        "description_vi": "Lệnh CREATE TABLE, ALTER TABLE, DROP TABLE, TRUNCATE TABLE, các kiểu dữ liệu Oracle (VARCHAR2, NUMBER, DATE, TIMESTAMP, ROWID, BLOB) và quy tắc đặt tên đối tượng."
    },
    4: {
        "title_vi": "Module 4: Ràng buộc toàn vẹn (Constraints)",
        "description_vi": "PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, cấp độ khai báo cột/bảng, mệnh đề CASCADE CONSTRAINTS, bật/tắt ràng buộc và từ điển dữ liệu USER_CONSTRAINTS."
    },
    5: {
        "title_vi": "Module 5: Ngôn ngữ thao tác dữ liệu (DML)",
        "description_vi": "Lệnh INSERT, UPDATE, DELETE, MERGE (UPSERT), chèn dữ liệu bằng truy vấn con, giao dịch cơ sở dữ liệu và xử lý ràng buộc khi thao tác dữ liệu."
    },
    6: {
        "title_vi": "Module 6: Hàm xử lý đơn dòng (Single Row Functions)",
        "description_vi": "Hàm chuỗi (LOWER, UPPER, INITCAP, TRIM, SUBSTR, LPAD), hàm số (ROUND, TRUNC, MOD), hàm ngày tháng (SYSDATE, ADD_MONTHS, TO_CHAR, TO_DATE) và hàm xử lý NULL (NVL, NVL2, NULLIF, DECODE)."
    },
    7: {
        "title_vi": "Module 7: Hàm nhóm & Gom nhóm dữ liệu (Group Functions)",
        "description_vi": "Hàm tổng hợp (COUNT, SUM, AVG, MIN, MAX), quy tắc xử lý NULL của hàm nhóm, mệnh đề GROUP BY, mệnh đề HAVING và phân biệt WHERE vs HAVING."
    },
    8: {
        "title_vi": "Module 8: Phép kết nối bảng (SQL Joins)",
        "description_vi": "Equijoin, Non-equijoin, Natural Join, USING clause, ON clause, Self Join, Outer Joins (LEFT, RIGHT, FULL OUTER JOIN), cú pháp truyền thống (+) và tích Descartes (Cartesian Product)."
    },
    9: {
        "title_vi": "Module 9: Truy vấn con cơ bản (Subqueries)",
        "description_vi": "Khái niệm Subquery, phân biệt Single-row subquery vs Multiple-row subquery (toán tử IN, ANY, ALL), vị trí sử dụng subquery và xử lý giá trị NULL trong NOT IN."
    },
    10: {
        "title_vi": "Module 10: Truy vấn con nâng cao (Advanced Subqueries)",
        "description_vi": "Truy vấn con tương quan (Correlated Subquery), toán tử EXISTS / NOT EXISTS, truy vấn con nhiều cột (Pairwise vs Non-pairwise), mệnh đề WITH (CTE) và Scalar Subquery."
    },
    11: {
        "title_vi": "Module 11: Khung nhìn (Views)",
        "description_vi": "Khái niệm View, tạo View đơn giản & phức tạp, tùy chọn FORCE, mệnh đề WITH CHECK OPTION, WITH READ ONLY, quy tắc DML trên View và truy vấn từ điển dữ liệu USER_VIEWS."
    },
    12: {
        "title_vi": "Module 12: Toán tử tập hợp & Cột giả (Set Operators & Pseudocolumns)",
        "description_vi": "Toán tử UNION, UNION ALL, INTERSECT, MINUS, quy tắc kết hợp SELECT, bảng DUAL, các cột giả ROWNUM, ROWID, LEVEL, NEXTVAL, CURRVAL và kỹ thuật Top-N Analysis."
    },
    13: {
        "title_vi": "Module 13: Chuẩn hóa cơ sở dữ liệu (Normalization)",
        "description_vi": "Khái niệm phụ thuộc hàm (Functional Dependency), các dạng dị thường dữ liệu (Insertion, Update, Deletion Anomaly), thuộc tính khóa và các dạng chuẩn 1NF, 2NF, 3NF, BCNF, DKNF."
    }
}
