# Hướng dẫn dự án BA (Chắt lọc từ BA-Kit)

Dự án này sử dụng bộ kỹ năng và quy tắc nghiệp vụ dành riêng cho quy trình IT BA phục vụ dự án khách hàng.

## 1. Các lệnh (Skills) khả dụng

| Lệnh | Vai trò | Mục đích |
|---|---|---|
| `/brainstorm` | Làm rõ yêu cầu thô | Phá vỡ sự mơ hồ, bẫy các câu hỏi mở (Open Questions), giả định và rủi ro |
| `/brd` | Business Requirements Document | Xác định bài toán kinh doanh, phạm vi (Scope), mục tiêu và Business Rules cốt lõi |
| `/urd` | User Requirements Document | Xác định Actor, nhu cầu thực tế và hành trình của người dùng cuối |
| `/srs` | Software Requirements Spec | Đặc tả chức năng (FR), phi chức năng (NFR), mã lỗi và logic chi tiết cho Dev |
| `/activity` | Activity Diagram | Dựng sơ đồ phân làn luồng xử lý (Swimlane) bằng Mermaid |
| `/user-flow` | User Flow | Sơ đồ luồng di chuyển qua các màn hình của người dùng |
| `/wireframe-html` | Khung giao diện HTML | Mô tả layout, các trường nhập liệu và trạng thái rỗng/lỗi cho Designer |
| `/userstory` | User Story & AC | Bóc tách FR thành các User Story kèm tiêu chí nghiệm thu Acceptance Criteria |
| `/test-checklist` | Ma trận kiểm thử | Quét độ phủ các kịch bản kiểm thử (Happy path, validation, boundary) cho QC |
| `/test-cases` | Bảng kịch bản test | Chi tiết hóa thành các bước kiểm thử (Precondition, Steps, Expected Result) |

## 2. Thứ tự luồng làm việc khuyến nghị

```text
/brainstorm ➔ /brd ➔ /urd ➔ /srs ➔ /activity hoặc /user-flow ➔ /wireframe-html ➔ /userstory ➔ /test-checklist ➔ /test-cases
```

## 3. Cấu trúc lưu trữ tài liệu
Mọi tài liệu đầu ra được lưu theo cấu trúc:
```text
docs/{feature}/
  ├── {feature}-brainstorm.md
  ├── {feature}-brd.md
  ├── {feature}-urd.md
  ├── {feature}-srs.md
  ├── wireframe/
  │     └── index.html
  └── tests/
        ├── test-checklist.md
        └── test-cases.md
```

## 4. Quy ước cốt lõi
1. **Approval Gate**: Luôn xin phép và hiển thị tóm tắt/diff trước khi tạo hoặc ghi đè file.
2. **Không tự bịa nghiệp vụ**: Nếu yêu cầu chưa rõ, bắt buộc phải ghi vào mục *Open Questions* để hỏi lại, tuyệt đối không tự phỏng đoán Business Rule.
3. **Mã định danh nhất quán**: Tuân thủ quy ước đặt mã `FR-{FEATURE}-{NUM}`, `BR-{FEATURE}-{NUM}`, `US-{FEATURE}-{NUM}`.
