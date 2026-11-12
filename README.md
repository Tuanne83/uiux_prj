# Kiosk & Web Registration System — BA Workspace

Dự án phân tích nghiệp vụ cho hệ thống tiếp đón, đăng ký khám bệnh qua **Ki-ốt đặt tại sảnh** và **Cổng web đặt lịch** tại Bệnh viện Đa khoa Huyện miền núi phía Bắc, Việt Nam.

**Khóa học:** IT4441E (HUST 2026.1)

---

## 🎯 Vấn đề giải quyết

- 📊 **Quá tải quầy tiếp đón:** 300–500 bệnh nhân/ngày vào buổi sáng
- 🌐 **Mạng chập chờn:** Cần offline mode + lưu tạm
- 👥 **Dân số đa dân tộc:** Giao diện trực quan + hỗ trợ giọng nói
- 🎫 **Đa loại định danh:** Chip CCCD mới + QR VNeID + thẻ BHYT giấy cũ

---

## 📚 Stack & Quy trình

**BA-Kit Framework** (Claude Code skills):
```
/brainstorm → /urd → /brd → /srs → /activity → /user-flow → /wireframe-html → /userstory → /test-checklist → /test-cases
```

**10 Skill khả dụng** trong dự án này:
- `/brainstorm` — Rà phát hiện & Open Questions
- `/urd` — Nhu cầu người dùng
- `/brd` — Mục tiêu kinh doanh & scope
- `/srs` — Yêu cầu kỹ thuật chi tiết
- `/activity` — Sơ đồ hoạt động (Mermaid)
- `/user-flow` — Luồng màn hình & phân chia flow
- `/wireframe-html` — Khung giao diện (HTML B&W)
- `/userstory` — Bóc FR thành user story
- `/test-checklist` — Ma trận kịch bản kiểm thử
- `/test-cases` — Chi tiết test case

---

## 🏗️ Cấu trúc thư mục

```
docs/
├── _shared/                    # Chung cho toàn dự án
│   ├── project-profile.md      # Bối cảnh (domain, người dùng, compliance)
│   ├── changelog.md            # Nhật ký thay đổi (auto-gen)
│   └── staleness.md            # Cảnh báo tài liệu cũ
│
└── kiosk-registration/         # Feature: Kiosk & Web Registration
    ├── brainstorms/
    │   └── kiosk-web-registration.md
    ├── srs/                    # (sẽ tạo sau)
    ├── html-wireframe/         # (sẽ tạo sau)
    └── userstories/            # (sẽ tạo sau)

.claude/
├── settings.json               # Cấu hình harness
├── rules/                      # 8 rule chung
│   ├── ba-conventions.md
│   ├── naming-conventions.md
│   ├── approval-gate.md
│   └── ... (5 files khác)
└── skills/                     # 10 skill BA
    ├── brainstorm/
    ├── urd/
    ├── ... (8 skills khác)
    └── kg/engine/              # Knowledge Graph engine
```

---

## 🚀 Bắt đầu

### 1. Cài đặt

```bash
# Clone repo
git clone <repo-url>
cd uiux_prj

# Kiểm tra Node.js (cần ≥18)
node --version

# Cài dependencies (cho kg-engine + mermaid-verify)
cd .claude/skills/kg/engine
npm install
cd ../../../

# Mở trong Claude Code
claude .
```

### 2. Chạy skill đầu tiên

```bash
# Trong Claude Code terminal
/user-flow kiosk-registration
```

### 3. Xem kết quả

Output sẽ viết vào:
```
docs/kiosk-registration/srs/kiosk-registration-userflow.md
```

---

## 📖 Quy ước Dự án

**⚠️ Bắt buộc đọc trước khi chỉnh sửa:**

1. **`CLAUDE.md`** — Approval-gate (L1 plan trước Write, L2 diff trước Edit)
2. **`.claude/rules/ba-conventions.md`** — Không tự bịa dữ liệu, không hỏi lại
3. **`.claude/rules/approval-gate.md`** — L1/L2/L3 approval process

**Ngắn gọn:**
- ✅ Mỗi file phải có frontmatter (type, feature, status, updated, links)
- ✅ ID format: `FR-{feature}-NNN`, `E-{feature}-NNN`
- ✅ Mermaid diagram phải qua `mermaid-verify.mjs`
- ✅ Không commit `.claude/state/` (chứa secret)

---

## 📊 Bối cảnh Dự án

**Domain:** Tiếp đón + đăng ký khám bệnh tự phục vụ qua ki-ốt + web  
**Người dùng:** Bệnh nhân, người nhà, nhân viên tiếp đón, lãnh đạo BV  
**Compliance:** 11 nghị định/thông tư 2025-2026 (xem `docs/_shared/project-profile.md`)  
**Phạm vi:** Khám ngoài trú (KHÔNG cấp cứu)  

**Quyết định chốt:**
- ✅ Ki-ốt đọc **chip CCCD** (RAR chứng nhận)
- ✅ 1 lớp hàng đợi duy nhất
- ✅ 3 nhánh xử lý nơi ĐK khác (C1/C2/C3: phiếu e / phiếu giấy / thông cấp)

---

## 🔧 Troubleshooting

### Mermaid diagram báo lỗi cú pháp

```bash
node .claude/scripts/mermaid-verify.mjs --file docs/kiosk-registration/srs/{feature}-flows.md
```

### Changelog không update

Kiểm tra `.claude/hooks/auto-changelog.sh` (xem `settings.json` → `hooks`)

### Tài liệu bị "stale" (cảnh báo cũ)

Chạy `/gap kiosk-registration` để xem liên hệ giữa docs

---

## 📋 Next Steps

1. ✅ **Brainstorm:** `docs/kiosk-registration/brainstorms/kiosk-web-registration.md`
2. ⬜ **URD:** `/urd kiosk-registration`
3. ⬜ **BRD:** `/brd kiosk-registration`
4. ⬜ **SRS:** `/srs kiosk-registration`
5. ⬜ **Activity diagram:** `/activity "tên flow" --feature kiosk-registration`
6. ⬜ **User flow:** `/user-flow kiosk-registration`
7. ⬜ **Wireframe:** `/wireframe-html kiosk-registration`
8. ⬜ **User story:** `/userstory kiosk-registration`
9. ⬜ **Test checklist:** `/test-checklist kiosk-registration`
10. ⬜ **Test cases:** `/test-cases kiosk-registration`

---

## 🤝 Đóng góp

- Mở **GitHub Issues** để báo cáo hoặc đề xuất
- Tạo **Pull Request** từ nhánh `feature/*` hoặc `fix/*`
- Tuân theo quy ước tại `CLAUDE.md`

---

**Đội dự án:** IT4441E, HUST 2026.1  
**Liên hệ:** Xem `GETTING_STARTED.md` để setup lần đầu