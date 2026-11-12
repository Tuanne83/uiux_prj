# BA Workspace — Quy trình Phân tích Nghiệp vụ

> Tài liệu cấu hình cho dự án phần mềm khách hàng. Mọi tài liệu phân tích được lưu theo feature tại `docs/{feature-slug}/`.

## 1. Cấu trúc thư mục dự án

```text
.
├── CLAUDE.md                        ← Tài liệu quy ước cho Claude Code
├── GEMINI.md                        ← Quy tắc & ánh xạ công cụ cho Antigravity
├── .claude/                         ← Cấu hình & skill cho Claude Code
│   ├── settings.json                ← Quyền truy cập + lifecycle hooks
│   ├── hooks/                       ← Hook tự động (changelog, staleness, status, kg-refresh)
│   ├── rules/                       ← 16 rule nghiệp vụ & quy ước chung
│   ├── skills/                      ← 10 skill đã chọn + engine KG (.claude/skills/kg/engine/)
│   ├── agents/                      ← 8 review agent độc lập
│   └── scripts/                     ← Script kiểm tra cú pháp Mermaid (mermaid-verify.mjs)
├── .agents/                         ← Bản tương thích cho Antigravity (IDE / CLI)
│   ├── hooks.json + hooks/          ← Adapter chạy PostToolUse hooks khi ghi/sửa docs/
│   ├── skills/                      ← 10 skill (đồng bộ từ .claude/skills/)
│   ├── rules/                       ← 16 rule (đồng bộ từ .claude/rules/)
│   ├── agents/                      ← 8 review agent (đồng bộ từ .claude/agents/)
│   └── scripts/                     ← mermaid-verify.mjs
├── _templates/                      ← Khung mẫu Markdown/HTML cho 10 skill
├── _scripts/                        ← Helper kiểm tra trạng thái workspace (workspace-status.py)
└── docs/                            ← Toàn bộ tài liệu BA đầu ra (sinh trong quá trình làm dự án)
    ├── _shared/                     ← Dùng chung toàn dự án
    │   ├── project-profile.md       ← Bối cảnh dự án (domain, thuật ngữ, compliance)
    │   ├── changelog.md             ← Nhật ký thay đổi tự động (append-only)
    │   ├── staleness.md             ← Cảnh báo tài liệu downstream bị cũ khi upstream đổi
    │   └── kg/                      ← Chỉ mục Knowledge Graph (sinh tự động bởi kg-build/query)
    └── {feature-slug}/              ← Thư mục riêng cho từng tính năng
        ├── brainstorms/{idea}.md              ← Output của /brainstorm
        ├── {feature}-brd.md                   ← Output của /brd
        ├── {feature}-urd.md                   ← Output của /urd
        ├── srs/
        │   ├── {feature}-spec.md              ← Output của /srs (FR, NFR, BR, Error Matrix)
        │   ├── {feature}-flows.md             ← Output của /activity (Activity Diagram)
        │   └── {feature}-userflow.md          ← Output của /user-flow
        ├── html-wireframe/                    ← Output của /wireframe-html
        │   ├── {feature}-wireframe-html-index.md
        │   ├── {feature}-wireframe.html
        │   └── {flow-slug}.html
        ├── userstories/                       ← Output của /userstory
        │   ├── {feature}-story-index.md
        │   └── us-{NNN}.md
        └── test/                              ← Output của /test-checklist & /test-cases
            ├── checklist/{feature}-checklist-index.md
            └── testcases/{feature}-testcase-index.md
```

## 2. Danh sách 10 Skill khả dụng & Thứ tự sử dụng

Pipeline chuẩn từ lúc nhận yêu cầu thô của khách hàng đến khi bàn giao cho Dev, Designer và QC:

```text
/brainstorm ➔ /brd ➔ /urd ➔ /srs ➔ /activity hoặc /user-flow ➔ /wireframe-html ➔ /userstory ➔ /test-checklist ➔ /test-cases
```

| Lệnh | Đầu vào chính | Đầu ra | Mục đích |
|---|---|---|---|
| `/brainstorm [<ý tưởng>]` | Yêu cầu thô / ghi chú | `brainstorms/{idea}.md` | Làm rõ đề bài, phát hiện giả định ngầm, bẫy edge case và Open Questions |
| `/brd [<feature>]` | Brainstorm | `{feature}-brd.md` | Xác định mục tiêu kinh doanh, phạm vi (In/Out-scope), Business Rules cốt lõi |
| `/urd [<feature>]` | Brainstorm / BRD | `{feature}-urd.md` | Chân dung người dùng (Actor/Persona), nhu cầu, hành trình & kỳ vọng thành công |
| `/srs [<feature>]` | BRD / URD / Brainstorm | `srs/{feature}-spec.md` | Đặc tả chức năng (FR), phi chức năng (NFR), Business Rules (BR) và Error Matrix cho Dev |
| `/activity "<mô tả>" --feature <slug>` | SRS | `srs/{feature}-flows.md` | Vẽ Activity Diagram (Mermaid) mô tả luồng xử lý, điều kiện rẽ nhánh & kiểm cú pháp |
| `/user-flow <feature>` | SRS | `srs/{feature}-userflow.md` | Thiết kế luồng màn hình (happy/error/edge) kèm review bởi `@flow-reviewer` |
| `/wireframe-html <feature>` | User flow + SRS | `html-wireframe/*.html` | Sinh khung wireframe HTML trắng đen kèm bảng mô tả chi tiết cho Designer |
| `/userstory [<feature>]` | SRS | `userstories/us-*.md` | Bóc FR thành User Story kèm Acceptance Criteria (AC) để quản lý backlog |
| `/test-checklist <feature>` | SRS + User story | `test/checklist/*.md` | Lập ma trận kịch bản kiểm thử (Happy path, validation, boundary, error) |
| `/test-cases <feature>` | Test checklist | `test/testcases/*.md` | Sinh bảng test case chi tiết 1:1 cho QC thực thi kiểm thử |

> **Lưu ý khi chạy `/srs`:** Trong project này chỉ giữ các skill nêu trên (không giữ `usecase`, `sequence`, `erd`, `state`, `wireframe-ascii`, `ac`, `jira`). Khuyến nghị chạy `/srs <feature> --spec-only` (Tầng 1 Core spec), sau đó chạy lần lượt `/activity`, `/user-flow`, `/wireframe-html`, `/userstory` để đảm bảo mỗi bước dùng đúng skill chuyên biệt hiện có.

## 3. Agents Review đi kèm (`.claude/agents/`)

Các agent phản biện đọc ở ngữ cảnh độc lập trước khi chốt tài liệu:
* `@senior-ba`, `@po-reviewer`, `@pm-reviewer`: Review BRD, URD, SRS về tính đầy đủ, phạm vi, giá trị kinh doanh và phụ thuộc.
* `@qa-reviewer`, `@tech-reviewer`, `@uxui-reviewer`: Review SRS và luồng giao diện về khả năng kiểm thử (testability), tính khả thi kỹ thuật và trạng thái màn hình (loading/empty/error).
* `@flow-reviewer`, `@diagram-reviewer`: Kiểm tra logic User Flow và tính đúng đắn của sơ đồ Activity/Mermaid.

## 4. Quy ước & Cổng kiểm soát (Rules)

* **Approval Gate (`.claude/rules/approval-gate.md`)**: Bắt buộc trình bày kế hoạch (L1 Plan) trước khi tạo file và hiển thị diff (L2 Diff) trước khi sửa file đã tồn tại. Không tự ý ghi file khi chưa có xác nhận.
* **Không tự bịa nghiệp vụ (`.claude/rules/ba-conventions.md`, `resolve-oqs.md`)**: Nếu thiếu thông tin hoặc chưa chốt rule, bắt buộc ghi vào **Open Questions** hoặc đánh dấu `[NEEDS CLARIFICATION: ...]` để hỏi lại, tuyệt đối không tự điền giả định. Không hỏi lại thông tin đã có ở tài liệu trước hoặc trong `docs/_shared/project-profile.md`.
* **Quy ước đặt tên & ID (`.claude/rules/naming-conventions.md`)**:
  * Tên feature dùng `kebab-case` (ví dụ `quan-ly-don-hang`).
  * ID gắn prefix theo feature: `FR-{feature}-NNN`, `NFR-{feature}-NNN`, `BR-{feature}-NNN`, `E-{feature}-NNN`, `BO-{feature}-NN`.
  * Frontmatter tối giản: `type`, `feature`, `status` (`draft → in-review → revisions → approved → shipped` hoặc `stale`), `updated`, `links`.
* **Kiểm tra Mermaid**: Mọi file có sơ đồ Mermaid phải chạy `node .claude/scripts/mermaid-verify.mjs --file <đường-dẫn>` sau khi ghi.
* **Nhật ký & Cảnh báo cũ**: Mọi chỉnh sửa trong `docs/` được hook tự động ghi vào `docs/_shared/changelog.md` và đánh dấu `stale` sang tài liệu phụ thuộc trong `docs/_shared/staleness.md`.
