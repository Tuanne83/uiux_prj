# 🎯 Getting Started — Hướng dẫn Lần Đầu

Bài hướng dẫn này dành cho **các thành viên mới** clone repo lần đầu tiên.

---

## 📥 Bước 1: Clone & Setup

```bash
# Clone repo
git clone <repo-url>
cd uiux_prj

# Kiểm tra phiên bản Node.js
node --version    # Cần ≥18.0.0

# (Nếu chưa có Node.js: cài từ https://nodejs.org/)
```

---

## 📖 Bước 2: Đọc quy ước dự án (5 phút)

**Bắt buộc trước khi chỉnh sửa bất kỳ file nào:**

1. **`CLAUDE.md`** — Approval-gate (L1/L2 process)
   - L1: **In bảng plan** trước khi tạo file mới
   - L2: **Show diff** trước khi sửa file có sẵn
   
2. **`.claude/rules/ba-conventions.md`**
   - Không tự bịa dữ liệu nghiệp vụ
   - Không hỏi lại câu đã trả lời (no-re-ask)
   - Business language, không hỏi technical (DB, SDK, endpoint)

3. **`.claude/rules/approval-gate.md`**
   - 3 levels: L1 (Plan), L2 (Diff), L3 (Iterate)
   - Khi nào cần gì

---

## 🧠 Bước 3: Hiểu bối cảnh dự án (10 phút)

Đọc file này theo thứ tự:

```
docs/_shared/project-profile.md
↓
.claude/projects/.../memory/
  ├── MEMORY.md (index)
  ├── project_domain.md (domain + người dùng)
  ├── business_flows.md (3 luồng A, B, C)
  ├── compliance_stack.md (11 nghị định/thông tư)
  └── key_decisions.md (quyết định chốt)
```

**Sơ bộ:**
- **Domain:** Tiếp đón + đăng ký khám bệnh tự phục vụ qua ki-ốt + web
- **Người dùng:** Bệnh nhân, người nhà, nhân viên tiếp đón, lãnh đạo BV
- **Quyết định chốt:** Ki-ốt đọc chip CCCD, 1 lớp hàng đợi, 3 nhánh xử lý chuyển cơ sở

---

## 🚀 Bước 4: Chạy skill đầu tiên

```bash
# Mở Claude Code
claude .

# Trong terminal Claude Code, chạy:
/brainstorm kiosk-registration
```

**Output:** `docs/kiosk-registration/brainstorms/kiosk-web-registration.md`

---

## 🔍 Bước 5: Kiểm tra Mermaid diagram (nếu cần)

Nếu chạy skill tạo diagram (vd `/activity`, `/user-flow`), phải kiểm tra:

```bash
# Kiểm tra cú pháp Mermaid
node .claude/scripts/mermaid-verify.mjs --file docs/kiosk-registration/srs/kiosk-registration-flows.md
```

**Expected:** `✓ Syntax OK | Verification: ...`

---

## 🔧 Troubleshooting

### Node.js không tìm được

```bash
# Cài nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Cài Node 18+
nvm install 18
nvm use 18
```

### mermaid-verify báo lỗi

**Lỗi 1:** Command không tìm thấy
```bash
# Kiểm tra path đến script
ls .claude/scripts/mermaid-verify.mjs

# Cài npm packages (nếu chưa)
cd .claude/skills/kg/engine && npm install && cd ../../../
```

**Lỗi 2:** Diagram lỗi cú pháp
- Kiểm tra file Mermaid: trích dòng lỗi từ output
- So sánh với ví dụ ở `docs/` hoặc `~/claude/projects/.../memory/business_flows.md`

### Claude Code không tìm thấy skill

```bash
# Reload Claude Code
Ctrl+C (quit)
claude .    (restart)
```

Hoặc:
- Mở **Command Palette** (Ctrl+Shift+P)
- Gõ "Claude: Reload"

---

## 📝 Quy trình thường ngày

### Khi muốn sửa / tạo doc mới

1. **Đọc quy ước** (CLAUDE.md + rules nếu chưa biết)
2. **Chạy skill tương ứng:**
   - Ý tưởng mới → `/brainstorm "description"`
   - Nhu cầu người dùng → `/urd kiosk-registration`
   - Mục tiêu kinh doanh → `/brd kiosk-registration`
   - Yêu cầu kỹ thuật → `/srs kiosk-registration`
   - Sơ đồ hoạt động → `/activity "tên luồng" --feature kiosk-registration`
   - Luồng màn hình → `/user-flow kiosk-registration`
   - Wireframe HTML → `/wireframe-html kiosk-registration`
   - User story → `/userstory kiosk-registration`
   - Test checklist → `/test-checklist kiosk-registration`
   - Test case → `/test-cases kiosk-registration`

3. **Skill sẽ hỏi approval (L1 Plan)**
   - In bảng dự định tạo/sửa file nào
   - Bạn xác nhận `Y` / `n` / `select...`

4. **Nếu sửa file có sẵn, skill hỏi L2 Diff**
   - Hiển thị `+++` / `---` thay đổi
   - Bạn xác nhận `Y` / `n`

5. **Skill viết file + tự động:**
   - Ghi vào `docs/_shared/changelog.md`
   - Cập nhật Knowledge Graph
   - Cảnh báo file downstream bị cũ (staleness.md)

### Khi muốn push lên git

```bash
# Kiểm tra tình trạng
git status

# Add các file cần thiết (giữ nguyên quy ước .gitignore)
git add docs/ .gitignore README.md GETTING_STARTED.md

# Commit
git commit -m "Describe what you changed"

# Push
git push origin main
```

---

## 🆘 Cần giúp?

| Vấn đề | Làm gì |
|---|---|
| Không hiểu skill nào dùng | Đọc `README.md` mục "Next Steps" (pipeline tuần tự) |
| Lỗi Mermaid syntax | Chạy `mermaid-verify.mjs` → xem error message |
| Không biết quy ước | Đọc `CLAUDE.md` + 8 files trong `.claude/rules/` |
| Muốn thay đổi docs có sẵn | Đọc `CLAUDE.md` mục "Approval-gate" (L1/L2 process) |
| Câu hỏi mở (chưa chốt thông tin) | Ghi vào "Open Questions (OQ)" trong brainstorm |
| Liên hệ compliance / pháp lý | Xem `docs/_shared/project-profile.md` mục Compliance |

---

## 📚 Tài liệu tham khảo

| File | Nội dung |
|---|---|
| `CLAUDE.md` | Quy ước & Approval-gate |
| `.claude/rules/ba-conventions.md` | Quy ước BA chung (no-re-ask, business language) |
| `.claude/rules/naming-conventions.md` | Đặt tên file, folder, ID |
| `.claude/rules/approval-gate.md` | L1/L2/L3 approval process |
| `docs/_shared/project-profile.md` | Bối cảnh dự án (domain, compliance, người dùng) |
| `.claude/projects/.../memory/` | Memory files (project domain, flows, compliance, decisions) |

---

**Sẵn sàng bắt đầu!** 🎉

Nếu bị kẹt, mở **GitHub Discussions** hoặc đọc lại phần **Troubleshooting** ở trên.

---

*Cập nhật lần cuối: 2026-11-12*
