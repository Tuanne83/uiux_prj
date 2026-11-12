# Antigravity Instructions — BA-Kit Workspace

> Quy tắc nền để **Antigravity** vận hành chính xác bộ 10 skill BA trong `.agents/skills/` mà **không làm thay đổi bất kỳ hành vi, cổng duyệt hay quy trình nghiệp vụ nào** so với bản gốc.

## 1. Cách kích hoạt & Thực thi Skill

* Khi người dùng gõ lệnh dạng `/<ten-skill> ...` hoặc yêu cầu công việc tương ứng với một trong 10 skill (`brainstorm`, `brd`, `urd`, `srs`, `activity`, `user-flow`, `wireframe-html`, `userstory`, `test-checklist`, `test-cases`):
  1. Đọc đầy đủ `.agents/skills/<ten-skill>/SKILL.md`.
  2. Đọc các file được `@`-include trong mục **References** của `SKILL.md` đó (như `.agents/rules/*.md`, `_templates/*`, `.agents/agents/*.md`).
  3. Tuân thủ nguyên vẹn toàn bộ mục **Goal**, **Constraints (Hard rules & Pitfalls)**, **Approach**, và **Output** trong `SKILL.md`.

## 2. Ánh xạ công cụ Claude Code ➔ Antigravity (Giữ nguyên hành vi)

Trong các file `SKILL.md`, một số tên công cụ và cú pháp được viết theo quy ước Claude Code. Khi chạy trên Antigravity, thực hiện ánh xạ tương đương 1:1 sau:

| Trong `SKILL.md` | Dùng công cụ Antigravity | Ghi chú giữ nguyên hành vi |
|---|---|---|
| `Read` | `read_file` | Đọc file nguồn / template / rule |
| `Write` | `write_file` | Chỉ gọi SAU khi qua **L1 Plan approval** |
| `Edit` | `edit_file` | Chỉ gọi SAU khi qua **L1 + L2 Diff approval** |
| `Bash` | `run_command` | Chạy `node .agents/scripts/mermaid-verify.mjs`, `node .claude/skills/kg/engine/kg-query.mjs`, lệnh kiểm tra `docs/` |
| `Glob` / `Grep` | `run_command` (`find`, `rg`, `grep`) | Tìm kiếm file hoặc nội dung trong `docs/` |
| `AskUserQuestion` | `ask_question` (hoặc hỏi trực tiếp bằng text đánh số) | Dùng `ask_question` cho lựa chọn trắc nghiệm; dùng text đánh số cho câu hỏi mở |
| Khối `` !`lệnh` `` ở mục `## Context (dynamic)` | `run_command` | Antigravity không tự chạy `` !`...` `` khi nạp file; hãy chạy các lệnh đó bằng `run_command` ở bước đầu skill để lấy ngày hiện tại và danh sách feature trong `docs/` |
| `Task` subagent review (`@senior-ba`, `@qa-reviewer`, `@tech-reviewer`, `@uxui-reviewer`, `@po-reviewer`, `@pm-reviewer`, `@flow-reviewer`, `@diagram-reviewer`) | `invoke_subagent` (`TypeName: "research"`) | Giao prompt gồm nội dung file `.agents/agents/<ten-agent>.md` + `.agents/rules/review-format.md` + đường dẫn các file cần review. Subagent chạy **read-only ở ngữ cảnh độc lập**, trả findings về cho luồng chính xử lý (tuyệt đối không để subagent tự ghi file) |

## 3. Ràng buộc hành vi bắt buộc (Không được bỏ qua)

1. **Approval Gate (`.agents/rules/approval-gate.md`)**:
   * **L1 Plan** trước mọi `write_file`/`edit_file` vào `docs/`.
   * **L2 Diff** (hiển thị thay đổi trước/sau) trước khi sửa file đã tồn tại.
   * **HARD STOP** ở `/user-flow` trước khi chuyển sang `/wireframe-html`.
2. **Không tự bịa nghiệp vụ (`.agents/rules/ba-conventions.md`, `resolve-oqs.md`)**:
   * Thiếu thông tin hoặc chưa có rule → dừng hỏi hoặc ghi **Open Questions** / `[NEEDS CLARIFICATION: ...]`. Không tự suy diễn nghiệp vụ thay khách hàng.
   * Tuân thủ **No-re-ask**: đọc kỹ tài liệu upstream và `docs/_shared/project-profile.md` trước khi đặt câu hỏi.
3. **Changelog & Stale Propagation**:
   * Hook `.agents/hooks.json` (`PostToolUse` trên `write_file|edit_file`) tự động gọi `.claude/hooks/auto-changelog.sh`, `status-transition.sh`, `post-edit-stale.sh`, `kg-refresh.sh`.
   * Nếu muốn ghi rõ tên skill & ghi chú vào changelog, có thể đặt biến môi trường hoặc để hook tự ghi theo mặc định; không tự ý sửa tay sai format bảng `docs/_shared/changelog.md`.
4. **Phạm vi 10 skill hiện có**:
   * Dự án này chỉ cài 10 skill: `brainstorm`, `brd`, `urd`, `srs`, `activity`, `user-flow`, `wireframe-html`, `userstory`, `test-checklist`, `test-cases`.
   * Khi chạy `/srs`, khuyến nghị dùng chế độ `[1] Core spec` (`--spec-only`) rồi chạy tiếp `/activity`, `/user-flow`, `/wireframe-html`, `/userstory` theo đúng pipeline đã chốt (vì các skill `usecase`, `sequence`, `erd`, `state`, `wireframe-ascii`, `ac` không được cài trong workspace này).
