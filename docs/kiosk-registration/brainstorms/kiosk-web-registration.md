---
type: brainstorm
feature: kiosk-registration
status: draft
updated: 2026-11-12
links:
  - IT4441E_ClientBriefing_B1.pptx.pdf
  - docs/_shared/project-profile.md
---

# Kiosk & Web Registration System — Brainstorm

## 1. Idea Seed

> Một bệnh viện đa khoa huyện ở vùng núi phía Bắc thường quá tải vào buổi sáng, hàng dài chờ ở quầy tiếp đón. Ban lãnh đạo bệnh viện muốn giảm tải bằng ki-ốt tự phục vụ ở sảnh và cổng đăng ký trên web.
> Sản phẩm giúp bệnh nhân lấy số thứ tự, kiểm tra bảo hiểm y tế, tìm đúng khoa và thanh toán nhanh, giảm hàng chờ ở quầy.

## 2. Context

- **Hiện trạng:** Quá tải trầm trọng vào khung giờ cao điểm buổi sáng (7h00 - 9h30). Bệnh nhân dồn ứ tại quầy tiếp đón tập trung.
- **Bối cảnh vùng cao (Constrained Context):**
  - Đồng bào dân tộc thiểu số (Mông, Dao, Tày...) chiếm tỷ lệ đáng kể; nhiều người cao tuổi khó khăn trong việc đọc và hiểu tiếng Việt phổ thông (H1).
  - Hạ tầng mạng Internet và lưới điện chập chờn, thường xuyên xảy ra sự cố mất điện / mất mạng đột ngột (H2).
  - Tỷ lệ người dân vẫn dùng thẻ BHYT bản giấy cũ còn cao, chưa đồng bộ thẻ căn cước gắn chip hoặc VNeID (H3). Lưu ý: cơ quan BHXH **đã dừng cấp thẻ BHYT bản giấy từ 01/6/2025** (Công văn 168/BHXH-QLT) — thẻ giấy cũ vẫn dùng đến hết hạn, nhưng người tham gia mới chỉ có thẻ điện tử trên VssID/VNeID hoặc dùng thẻ căn cước gắn chip. Ki-ốt vì vậy phải đọc được **cả ba** loại định danh.
  - Thói quen đi khám theo nhóm gia đình, một người thao tác bấm thay cho 3–4 người khác (H4).
  - Bệnh nhân ngại công khai thông tin bệnh lý tế nhị (sản phụ khoa, da liễu, truyền nhiễm...) nơi đông người (H5).
  - Trường hợp lấy số hộ cho người thân đang chờ ngoài xe hoặc ở nhà xa (H6).
  - Tâm lý phòng thủ, lo ngại bị mất việc hoặc xáo trộn vai trò của nhân viên tiếp đón có thâm niên (H7).
  - Bệnh nhân chỉ biết mô tả triệu chứng khó chịu (đau bụng, chóng mặt...) chứ không biết tên khoa khám bệnh tương ứng (H8).
  - Một phần bệnh nhân được trạm y tế xã chuyển lên, cầm theo phiếu chuyển cơ sở khám bệnh, chữa bệnh (bản giấy hoặc bản điện tử trên VNeID) (H9).
- **Ràng buộc:** Ngân sách thiết bị hạn chế (trang bị 01 ki-ốt cảm ứng ở sảnh trong giai đoạn 1); kết nối Cổng tiếp nhận dữ liệu giám định BHYT; giao diện tiếng Việt kèm hình minh họa và giọng nói hỗ trợ.

### 2.1 Căn cứ pháp lý đang áp dụng

> Danh mục này là nền của mọi quy tắc nghiệp vụ bên dưới. Mọi văn bản đều đã được rà hiệu lực tại thời điểm 12/11/2026.

| Lĩnh vực | Văn bản | Hiệu lực | Điều chi phối nghiệp vụ nào |
|---|---|---|---|
| Khám chữa bệnh | Luật Khám bệnh, chữa bệnh số **15/2023/QH15** | 01/01/2024 | Nhóm được ưu tiên khám trước; phân cấp chuyên môn kỹ thuật |
| Bảo hiểm y tế | Luật BHYT số 25/2008/QH12, sửa đổi bởi Luật số 46/2014/QH13 và Luật số **51/2024/QH15** | 01/7/2025 | Bỏ khái niệm "tuyến", chuyển sang **"cấp"**; mức hưởng; thay "mức lương cơ sở" bằng **"mức tham chiếu"** |
| Bảo hiểm y tế | Nghị định **188/2025/NĐ-CP** | 15/8/2025 | Hướng dẫn thi hành Luật BHYT. **Bãi bỏ toàn bộ** Nghị định 146/2018/NĐ-CP, 75/2023/NĐ-CP và 02/2025/NĐ-CP |
| Bảo hiểm y tế | Thông tư **01/2025/TT-BYT** (thay Thông tư 40/2015/TT-BYT) | 01/01/2025 | Đăng ký KCB ban đầu; chuyển cơ sở KCB; phiếu chuyển có giá trị **10 ngày làm việc**; Phụ lục I gồm 62 bệnh hiếm/hiểm nghèo; Phụ lục II bệnh mạn tính điều trị tại cấp cơ bản |
| Dữ liệu cá nhân | Luật Bảo vệ dữ liệu cá nhân số **91/2025/QH15** + Nghị định **356/2025/NĐ-CP** | 01/01/2026 | Dữ liệu sức khỏe là dữ liệu nhạy cảm; đồng ý và rút lại đồng ý; hồ sơ đánh giá tác động; dữ liệu trẻ em. **Thay thế Nghị định 13/2023/NĐ-CP đã hết hiệu lực** |
| Định danh | Luật Căn cước số **26/2023/QH15** | 01/7/2024 | Thẻ căn cước và số định danh cá nhân; thẻ CCCD cũ còn giá trị đến hết thời hạn |
| Bệnh án điện tử | Thông tư **13/2025/TT-BYT** (thay Thông tư 46/2018/TT-BYT) | 21/7/2025 | Bệnh viện phải triển khai hồ sơ bệnh án điện tử **chậm nhất 30/9/2025**; ki-ốt phải liên thông HIS/EMR |
| Hóa đơn | Nghị định **70/2025/NĐ-CP** sửa Nghị định 123/2020/NĐ-CP | 01/6/2025 | Thời điểm lập hóa đơn là thời điểm thu tiền; cơ sở y tế có phần mềm quản lý KCB và viện phí được tổng hợp hóa đơn điện tử cuối ngày cho người không lấy hóa đơn |
| Giá dịch vụ | Thông tư **21/2024/TT-BYT** | 01/01/2025 | **Phương pháp** định giá dịch vụ KCB. Giá cụ thể do HĐND cấp tỉnh quyết trong trần của Bộ Y tế — ki-ốt lấy giá từ bảng giá của bệnh viện, không gán cứng |
| Dữ liệu giám định | Quyết định **130/QĐ-BYT** (sửa đổi bởi Quyết định 4750/QĐ-BYT và 3176/QĐ-BYT) | 01/9/2023 | Chuẩn dữ liệu đầu ra XML gửi Cổng giám định BHYT |
| Quy trình khám | Quyết định **1313/QĐ-BYT** | 22/4/2013 | Khung quy trình khám bệnh tại Khoa Khám bệnh — dùng làm mốc đối chiếu thời gian chờ |

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| **Bệnh nhân người dân tộc / Cao tuổi** | Đọc chữ tiếng Việt chậm/kém, không rành công nghệ, không biết chọn khoa nào | Thao tác đơn giản qua biểu tượng hình ảnh, hỗ trợ giọng nói hướng dẫn, chỉ cần chọn triệu chứng |
| **Người nhà đại diện đi khám** | Đi cùng nhóm 3–4 người, vội về làm nương rẫy, hoặc lấy số hộ người đang chờ ở xa | Đăng ký liên tục cho nhiều người trong một phiên mà không bị nhầm lẫn hồ sơ, không bắt buộc người bệnh phải đứng trực tiếp trước ki-ốt |
| **Bệnh nhân được trạm y tế xã chuyển lên** | Cầm giấy chuyển cơ sở nhưng không biết phải đưa cho ai, sợ mất quyền lợi | Ki-ốt nhận diện được phiếu chuyển (điện tử hoặc giấy), chỉ dẫn rõ bước tiếp theo |
| **Nhân viên tiếp đón** | Áp lực giải quyết hàng dài mỗi sáng, tâm lý e ngại ki-ốt thay thế vị trí làm việc | Giảm tải thủ tục nhập liệu thủ công; chuyển vai trò sang hỗ trợ duyệt ca khó, xác minh BHYT, đối chiếu phiếu chuyển bản giấy và cấp phiếu dự phòng |
| **Điều dưỡng hướng dẫn** | Khó giải thích cho từng người giữa sảnh ồn ào hỗn loạn | Có công cụ ki-ốt trực quan để điều phối nhanh, giảm ùn tắc |
| **Lãnh đạo bệnh viện** | Thiếu dữ liệu phân luồng, quá tải quầy tiếp đón, ngân sách đầu tư thiết bị eo hẹp | Giảm tải rõ rệt tại quầy, chi phí đầu tư hợp lý, có báo cáo số liệu phân luồng khám bệnh |

## 4. Capabilities Breakdown

### P0 — must have

- Chọn ngôn ngữ / bật giọng nói trợ lý âm thanh ngay màn hình chào.
- **Đọc định danh đa phương thức tại ki-ốt:** đọc **chip thẻ căn cước** (thiết bị phải có tem chứng nhận RAR của C06 — Bộ Công an), quét **mã QR thẻ BHYT trên VssID/VNeID**, quét **mã vạch thẻ BHYT giấy** cũ, và nhập tay mã số BHYT khi thẻ mờ rách.
- **Tra cứu thẻ BHYT qua Cổng tiếp nhận dữ liệu giám định BHYT** — đọc định danh chỉ là bước 1, hệ thống phải tra cứu online để lấy: mã thẻ, họ tên, ngày sinh, giới tính, **mã nơi đăng ký KCB ban đầu**, **giá trị sử dụng (từ ngày — đến ngày)** và mức hưởng.
- **Kiểm tra giá trị sử dụng thẻ** theo quy định BHYT, phân biệt rõ 3 tình trạng: thẻ đang có giá trị; thẻ **chưa tới ngày có giá trị sử dụng**; thẻ hết hạn hoặc tạm dừng. Mỗi tình trạng có cách xử lý riêng (xem Mục 6.1 D11).
- **Kiểm tra nơi đăng ký KCB ban đầu và phiếu chuyển cơ sở KCB** (Luồng C, Mục 5.3) — đối chiếu mã nơi đăng ký ban đầu với mã cơ sở của bệnh viện; khác thì kích hoạt kiểm tra phiếu chuyển điện tử qua Cổng BHXH, hoặc chuyển quầy ưu tiên nếu bệnh nhân cầm phiếu bản giấy.
- **Nhận diện đối tượng ưu tiên theo Luật Khám bệnh, chữa bệnh số 15/2023/QH15**, tách làm 2 nhóm:
  - *Tự động theo ngày sinh* trả về từ cổng BHYT: trẻ em dưới 06 tuổi, người từ đủ 75 tuổi trở lên.
  - *Tự khai tại ki-ốt, xác minh tại quầy trước khi vào phòng khám*: phụ nữ có thai, người khuyết tật đặc biệt nặng, người khuyết tật nặng, người có công với cách mạng — ki-ốt **không suy được** các diện này từ dữ liệu thẻ.
  - Cả hai nhóm đều được cấp dãy số ưu tiên `UT-xxx`.
- Định tuyến phòng khám thông qua lựa chọn triệu chứng trực quan bằng hình ảnh (thay vì bắt buộc chọn tên khoa).
- **Xác định quyền lợi theo chính sách thông cấp** (Luật BHYT sửa đổi số 51/2024/QH15, Nghị định 188/2025/NĐ-CP): bệnh viện thuộc **cấp cơ bản**, người bệnh có thẻ còn giá trị sử dụng được hưởng quyền lợi ngay cả khi nơi đăng ký ban đầu ở cơ sở khác. Chỉ thu phí đầu buổi với: khám dịch vụ theo yêu cầu, người không có BHYT, thẻ hết hạn hoặc chưa có giá trị sử dụng.
- Thanh toán tiền công khám đầu buổi linh hoạt: quét mã QR động chuẩn ngân hàng tại ki-ốt (đối soát tự động trong 3 phút) HOẶC chọn "Đóng tiền mặt tại quầy" (in phiếu giữ số chờ thu ngân kích hoạt).
- **Xuất hóa đơn điện tử theo Nghị định 70/2025/NĐ-CP:** thời điểm lập hóa đơn là thời điểm thu tiền. Ki-ốt in phiếu thu, dữ liệu đẩy sang phần mềm quản lý viện phí; người bệnh không lấy hóa đơn thì hệ thống tổng hợp hóa đơn điện tử cuối ngày.
- **Bảo vệ dữ liệu cá nhân nhạy cảm** (Luật số 91/2025/QH15 và Nghị định 356/2025/NĐ-CP):
  - Phiếu in chỉ có Số thứ tự + Số phòng + Vị trí (Tầng/Khu nhà), không in tên khoa khám bệnh.
  - Màn hình ki-ốt che bớt chữ số giữa của số định danh/SĐT (`0123****8901`).
  - Màn hình hàng chờ và loa gọi **chỉ đọc số thứ tự, không đọc họ tên đầy đủ**.
  - Có màn hình thông báo xử lý dữ liệu + thu thập đồng ý ngay tại ki-ốt (không chỉ ở web).
  - Dữ liệu đệm cục bộ khi mất mạng phải được **mã hóa** và **tự xóa sau khi đồng bộ thành công**.
- **Liên thông HIS / hồ sơ bệnh án điện tử** (Thông tư 13/2025/TT-BYT): mỗi lượt đăng ký tại ki-ốt tạo đúng một hồ sơ trong HIS theo định danh bệnh nhân duy nhất, không sinh hồ sơ trùng; dữ liệu phục vụ giám định xuất theo chuẩn XML của Quyết định 130/QĐ-BYT (và các quyết định sửa đổi).
- Cổng web đăng ký khám bệnh từ xa: đăng ký tài khoản bằng số định danh cá nhân (kèm xác nhận đồng ý xử lý dữ liệu cá nhân và đường dẫn rút lại đồng ý), thêm hồ sơ người thân, chọn ngày và khung giờ khám.
- **Đồng ý của cha mẹ/người giám hộ khi thêm hồ sơ người dưới 16 tuổi** (Luật số 91/2025/QH15) và ghi nhận căn cứ đại diện khi một người đăng ký hộ người khác.
- Đặt lịch trên web: khám dịch vụ thanh toán phí khám trước qua QR trong vòng 10 phút; khám BHYT giữ chỗ trực tuyến và xác thực thẻ tại viện.
- Check-in tại ki-ốt bằng mã QR lịch hẹn đặt trước (in ngay số thứ tự đã cấp sẵn).
- Chế độ hoạt động ngoại tuyến khi mất mạng: lưu đệm cục bộ có mã hóa, in phiếu tạm "Thanh toán & xác minh tại quầy" và tự động đồng bộ khi có mạng trở lại.

### P1 — should have

- Xem bản đồ / sơ đồ chỉ đường đơn giản từ sảnh đến phòng khám hiển thị trên phiếu.
- Hỗ trợ đăng ký nhiều người (tối đa 4 người/phiên) cho người nhà đi cùng nhóm.
- Khi bệnh nhân đến trễ lịch hẹn web quá 20 phút: hủy quyền ưu tiên giờ hẹn, chuyển sang cấp số khám vãng lai (xếp cuối hàng hiện tại) nhưng tự động bảo lưu khoản tiền công khám đã đóng trên web (không thu tiền lại).
- Hủy lịch hẹn trước 12 tiếng trên web; yêu cầu hoàn tiền chuyển sang trạng thái **"Chờ duyệt hoàn"** để phòng Tài chính kế toán duyệt trước khi ngân hàng chuyển trả.
- Gọi số tự động qua hệ thống loa phát thanh tại khu chờ (gọi 2 lần trước khi chuyển qua lượt), chỉ đọc số.
- Màn hình quản trị tiếp đón dành cho nhân viên y tế (xem danh sách, tiếp nhận ca BHYT lỗi, **đối chiếu phiếu chuyển cơ sở bản giấy**, cấp phiếu giấy khi mất điện).
- Xác thực sinh trắc học (so khớp khuôn mặt với dữ liệu chip thẻ căn cước) để chống mượn thẻ BHYT.

### P2 — nice to have

- Tích hợp thêm tùy chọn giọng nói hướng dẫn bằng tiếng dân tộc thiểu số địa phương (Mông, Dao, Tày).
- Báo cáo phân tích thời gian chờ và tỷ lệ tự phục vụ dành cho ban giám đốc, đối chiếu với khung thời gian của Quyết định 1313/QĐ-BYT.
- Nạp tiền tạm ứng vào thẻ khám bệnh để trừ dần các chi phí cận lâm sàng (xét nghiệm, X-quang) sau khám.

### Ngoài phạm vi (Out of scope)

- **Cấp cứu** — người bệnh trong tình trạng cấp cứu đi thẳng khoa Cấp cứu, không qua ki-ốt. Ki-ốt chỉ hiển thị biển chỉ dẫn tĩnh tại màn hình chào.
- Khám sức khỏe định kỳ, khám tuyển dụng, tiêm chủng, lấy mẫu xét nghiệm theo yêu cầu.
- Thu viện phí nội trú, tạm ứng nhập viện, quyết toán ra viện.
- Cấp và ký phiếu chuyển cơ sở KCB đi tuyến trên (việc của bác sĩ trên HIS, không phải của ki-ốt).

## 5. Core Flows (Happy Path)

> Toàn bộ các luồng dùng **một lớp hàng đợi duy nhất**: số thứ tự ki-ốt cấp ra **chính là số khám tại phòng khám** đó. Không có số tiếp đón riêng rồi lấy số lần hai tại cửa phòng.

### 5.1 Luồng A — Tiếp đón và lấy số tại Ki-ốt (Khám vãng lai)

1. Bệnh nhân/người nhà chạm màn hình ki-ốt (có thể bấm nút nghe hướng dẫn âm thanh). Màn hình chào hiển thị đồng thời biển chỉ dẫn "Cấp cứu — đi thẳng khoa Cấp cứu, không lấy số" và thông báo xử lý dữ liệu cá nhân. Hệ thống hỏi: "Bạn đã đặt lịch trước chưa?". Bệnh nhân chọn "Chưa đặt lịch".
2. Bệnh nhân đặt **thẻ căn cước gắn chip** vào đầu đọc (hoặc quét mã QR thẻ BHYT trên VssID/VNeID, hoặc quét mã vạch thẻ BHYT giấy, hoặc nhập tay mã số BHYT).
3. Hệ thống tra cứu Cổng tiếp nhận dữ liệu giám định BHYT, lấy về: mã thẻ, họ tên, ngày sinh, giới tính, mã nơi đăng ký KCB ban đầu, giá trị sử dụng và mức hưởng.
4. Hệ thống kiểm tra **giá trị sử dụng thẻ** (xem D11) rồi chuyển sang **Luồng C** để đối chiếu nơi đăng ký KCB ban đầu và phiếu chuyển cơ sở.
5. Bệnh nhân chạm chọn vùng cơ thể / triệu chứng khó chịu qua các icon minh họa đơn giản. Hệ thống tự động gợi ý phòng khám phù hợp. Nếu thuộc diện ưu tiên tự khai (phụ nữ có thai, khuyết tật, người có công), bệnh nhân bấm chọn tại đây.
6. Hệ thống kiểm tra diện thu phí đầu buổi:
   - **Khám BHYT, thẻ đang có giá trị sử dụng:** bệnh viện thuộc cấp cơ bản nên người bệnh hưởng quyền lợi theo chính sách thông cấp. Chưa thu tiền ở bước lấy số (phần cùng chi trả được tính gộp cả đợt khám và đối chiếu ngưỡng theo **mức tham chiếu** vào cuối buổi) — bỏ qua bước thanh toán, in phiếu ngay.
   - **Khám dịch vụ theo yêu cầu / Không có BHYT / Thẻ hết hạn hoặc chưa có giá trị sử dụng:** hiển thị số tiền công khám lấy từ bảng giá của bệnh viện, kèm 2 lựa chọn: "Quét mã QR tại máy" hoặc "Đóng tiền mặt tại quầy".
7. Xử lý thanh toán (nếu thuộc diện thu phí đầu buổi):
   - **Quét mã QR:** bệnh nhân quét QR thanh toán trong vòng 3 phút, hệ thống đối soát thành công, ghi nhận thời điểm thu tiền để lập hóa đơn điện tử, in phiếu vào thẳng phòng khám.
   - **Tiền mặt tại quầy:** máy vẫn in phiếu giữ số thứ tự (trạng thái "Chờ thu ngân kích hoạt"), bệnh nhân cầm phiếu qua quầy thu ngân nộp tiền mặt mà không phải khai lại thông tin.
8. Máy in nhả phiếu số thứ tự (Số thứ tự + Số phòng + Tầng/Khu nhà, không in tên khoa). Hồ sơ được ghi vào HIS theo định danh bệnh nhân duy nhất. Bệnh nhân có thể chọn "Đăng ký tiếp cho người nhà" hoặc "Kết thúc".

```
[Chạm màn hình ki-ốt]
        │
        ▼
[Chọn "Chưa đặt lịch"]
        │
        ▼
[Đọc chip căn cước / QR VssID-VNeID / mã vạch thẻ giấy]
        │
        ▼
[Tra cứu Cổng giám định BHYT] ──▶ [Kiểm tra giá trị sử dụng thẻ]
        │
        ▼
[LUỒNG C: đối chiếu nơi ĐK ban đầu + phiếu chuyển]
        │
        ▼
[Chọn triệu chứng hình ảnh] ──▶ [Hệ thống gợi ý phòng khám]
        │
        ▼
[Kiểm tra diện thu phí đầu buổi]
        ├─▶ [BHYT, thẻ đang có giá trị (thông cấp)] ─────────────────┐
        └─▶ [Dịch vụ / Không BHYT / Thẻ không có giá trị]            │
                ├─▶ [Quét QR (3 phút)] ──(Đối soát OK)───────────────┤
                └─▶ [Tiền mặt tại quầy] ──(Phiếu chờ kích hoạt)──────┤
                                                                      ▼
                              [Ghi hồ sơ vào HIS + In phiếu: Số khám + Phòng + Tầng/Khu]
                                              │
                                              ▼
                                [Xem sơ đồ dẫn đường đến phòng]
```

### 5.2 Luồng B — Đăng ký trước qua Web Portal & Check-in tại Ki-ốt

1. Bệnh nhân/người nhà truy cập cổng web, đăng nhập bằng số định danh cá nhân và mật khẩu.
2. Chọn hồ sơ khám (bản thân hoặc người thân đã thêm trong danh sách gia đình). Hồ sơ người dưới 16 tuổi yêu cầu xác nhận đồng ý của cha mẹ/người giám hộ.
3. Chọn chuyên khoa/triệu chứng, chọn ngày khám và khung giờ còn trống (tối đa 1 lịch/chuyên khoa/ngày).
4. Hệ thống tạo phiếu hẹn tạm: khám dịch vụ thì hiển thị mã QR thanh toán tiền công khám trong 10 phút; khám BHYT thì xác nhận giữ chỗ và xác thực thẻ tại viện.
5. Hệ thống xác nhận đặt lịch thành công, cấp mã QR lịch hẹn kèm thông tin số phòng khám.
6. Vào ngày khám, bệnh nhân chạm màn hình ki-ốt và chọn "Đã đặt lịch" (nếu đến trễ > 20 phút, hệ thống hủy giờ ưu tiên nhưng bảo lưu tiền đã đóng trên web và cấp số thứ tự vãng lai mới).
7. Đưa mã QR trên điện thoại vào đầu đọc của ki-ốt. Ki-ốt kiểm tra hợp lệ, tra cứu lại giá trị sử dụng thẻ BHYT tại thời điểm khám, và in ngay phiếu số thứ tự đã cấp sẵn mà không cần thao tác lại.

```
[Truy cập Web Portal] ──▶ [Đăng nhập bằng số định danh]
         │
         ▼
[Chọn hồ sơ người khám] ──▶ [Chọn ngày + Khung giờ]
         │
         ▼
[Kiểm tra hình thức đặt lịch]
         ├─▶ [Khám BHYT: Xác nhận giữ chỗ (xác thực thẻ tại viện)] ──┐
         └─▶ [Khám dịch vụ: Quét QR thanh toán trong 10 phút] ───────┤
         │
         ▼
[Cấp mã QR lịch hẹn trên điện thoại]
         │
         ▼ (Vào ngày khám đến sảnh viện)
[Đến ki-ốt: Chạm "Đã đặt lịch"] ──▶ [Quét mã QR lịch hẹn]
         │
         ▼ (Hợp lệ, trễ <= 20 phút, thẻ còn giá trị)
[In ngay phiếu số thứ tự đã cấp sẵn]
```

### 5.3 Luồng C — Đối chiếu nơi đăng ký KCB ban đầu & Phiếu chuyển cơ sở

> Luồng này chạy chèn vào giữa Luồng A (sau bước tra cứu thẻ) và cũng chạy khi check-in ở Luồng B. Mục đích: ghi nhận đúng diện khám vào hồ sơ giám định và ưu tiên người cầm phiếu chuyển — **không phải để chặn người bệnh**.

1. Sau khi tra cứu thẻ, hệ thống lấy **mã nơi đăng ký KCB ban đầu** từ Cổng giám định BHYT.
2. So sánh với mã cơ sở của bệnh viện:
   - **Trùng** — ghi nhận diện "Đúng nơi đăng ký ban đầu", quay lại Luồng A bước 5.
   - **Khác** — kích hoạt kiểm tra phiếu chuyển cơ sở khám bệnh, chữa bệnh theo 3 kịch bản dưới.
3. **C1 — Phiếu chuyển điện tử:** ki-ốt gọi API tra cứu thông tin chuyển tuyến trên Cổng BHXH theo số định danh cá nhân.
   - Tìm thấy phiếu còn hiệu lực (trong 10 ngày làm việc kể từ ngày ký, theo Thông tư 01/2025/TT-BYT) → ghi mã phiếu vào hồ sơ khám, hiển thị "Đã nhận phiếu chuyển từ {tên cơ sở}", quay lại Luồng A bước 5 bình thường.
4. **C2 — Phiếu chuyển bản giấy:** không tìm thấy phiếu điện tử, ki-ốt hỏi "Cô/bác có mang giấy chuyển tuyến bản giấy không?".
   - Bệnh nhân chọn "Có" → ki-ốt in phiếu thuộc **dãy ưu tiên `CT-xxx`**, hướng dẫn đến quầy tiếp đón để nhân viên đối chiếu bản gốc và nhập mã phiếu vào hệ thống. Không bắt bệnh nhân xếp hàng chung.
5. **C3 — Không có phiếu chuyển:** bệnh nhân chọn "Không có".
   - Hệ thống **vẫn cấp số khám bình thường** theo chính sách thông cấp (bệnh viện thuộc cấp cơ bản), ghi nhận diện "Thông cấp — không có phiếu chuyển" vào hồ sơ giám định.
   - Màn hình hiển thị rõ quyền lợi được hưởng trước khi in phiếu, để tránh tranh cãi tại cửa phòng khám.
6. Trường hợp mất mạng không tra cứu được phiếu điện tử: xử lý như C2, in phiếu `CT-xxx` chuyển quầy.

```
[Tra cứu thẻ xong] ──▶ [Lấy mã nơi đăng ký KCB ban đầu]
            │
            ▼
   [So với mã cơ sở bệnh viện]
     ├─▶ TRÙNG ──▶ [Diện: Đúng nơi ĐK ban đầu] ──────────────────────┐
     └─▶ KHÁC                                                        │
          │                                                          │
          ▼                                                          │
   [Gọi API tra cứu phiếu chuyển điện tử - Cổng BHXH]                │
          ├─▶ C1: Có phiếu, còn hiệu lực 10 ngày làm việc            │
          │        └─▶ [Ghi mã phiếu vào hồ sơ] ────────────────────┤
          ├─▶ C2: Không có phiếu điện tử, bệnh nhân có bản GIẤY      │
          │        └─▶ [In phiếu ưu tiên CT-xxx] ──▶ [Quầy đối chiếu bản gốc]
          └─▶ C3: Không có phiếu nào                                 │
                   └─▶ [Diện: Thông cấp] + [Hiển thị quyền lợi] ─────┤
                                                                      ▼
                                                      [Tiếp tục chọn triệu chứng]
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | Ki-ốt | Bệnh nhân chạm màn hình | Đã đặt lịch trước → Chuyển sang luồng Quét QR lịch hẹn | Chưa đặt lịch → Chuyển sang luồng đọc định danh vãng lai |
| D2 | Ki-ốt | Tra cứu dữ liệu BHYT trên Cổng giám định | Tra cứu thành công → Ghi nhận mã thẻ, nơi ĐK ban đầu, giá trị sử dụng, mức hưởng | Sai thông tin / cổng lỗi / mất mạng → Chuyển diện thu phí tạm + ghi chú "Cần xác minh BHYT tại quầy" |
| D3 | Ki-ốt | Kiểm tra diện thu phí đầu buổi | Thẻ BHYT đang có giá trị sử dụng → Chưa thu tiền đầu buổi, in phiếu ngay | Khám dịch vụ / Không BHYT / Thẻ không có giá trị → Hiển thị số tiền kèm 2 lựa chọn: Quét QR hoặc Đóng tiền mặt tại quầy |
| D4 | Ki-ốt | Chọn phương thức đóng tiền | Quét QR và đối soát thành công trong 3 phút → Ghi thời điểm thu tiền, in phiếu vào thẳng phòng khám (Quá 3 phút → hủy giao dịch) | Đóng tiền mặt tại quầy → In phiếu giữ số thứ tự (trạng thái "Chờ thu ngân kích hoạt") |
| D5 | Ki-ốt | Đăng ký cho người tiếp theo | Chọn "Đăng ký thêm người nhà" → Lưu hồ sơ người trước, mở lại bước nhập thông tin người mới | Chọn "Kết thúc" → Đóng phiên, hiển thị màn hình sơ đồ dẫn đường |
| D6 | Ki-ốt | Check-in lịch hẹn web | Check-in đúng giờ (đến sớm hoặc trễ ≤ 20 phút) → In phiếu nhận số đã giữ | Trễ > 20 phút → Hủy giờ ưu tiên, bảo lưu tiền đã đóng trên web và in phiếu cấp số vãng lai mới (xếp cuối hàng) |
| D7 | Ki-ốt | Trạng thái kết nối mạng Internet | Có mạng bình thường → Tra cứu Cổng giám định BHYT, tra phiếu chuyển điện tử và thanh toán QR trực tuyến | Mất mạng → Kích hoạt chế độ ngoại tuyến, in phiếu tạm "Thanh toán & xác minh tại quầy", lưu đệm cục bộ có mã hóa |
| D8 | Web | Thanh toán đặt lịch khám | Thanh toán thành công trong 10 phút → Xác nhận lịch hẹn chính thức | Quá 10 phút chưa thanh toán → Tự động hủy lịch hẹn tạm, nhả lại khung giờ trống |
| D9 | Ki-ốt (Luồng C) | So mã nơi đăng ký KCB ban đầu với mã cơ sở bệnh viện | Trùng → Ghi diện "Đúng nơi đăng ký ban đầu", đi tiếp chọn triệu chứng | Khác → Kích hoạt kiểm tra phiếu chuyển cơ sở (D10) |
| D10 | Ki-ốt (Luồng C) | Kiểm tra phiếu chuyển cơ sở KCB | Có phiếu điện tử còn hiệu lực 10 ngày làm việc → Ghi mã phiếu vào hồ sơ, cấp số bình thường | Không có phiếu điện tử → Hỏi có bản giấy không: Có → in phiếu ưu tiên `CT-xxx` về quầy đối chiếu; Không → vẫn cấp số theo diện thông cấp, hiển thị quyền lợi |
| D11 | Ki-ốt | Kiểm tra giá trị sử dụng thẻ BHYT | Thẻ đang trong khoảng giá trị sử dụng → Xử lý theo diện BHYT | Thẻ **chưa tới ngày có giá trị** → Thông báo ngày bắt đầu hưởng, chuyển diện thu phí; Thẻ **hết hạn/tạm dừng** → Chuyển diện thu phí + ghi chú xác minh tại quầy; **Sai thông tin nhân thân** → Chuyển thẳng quầy tiếp đón |
| D12 | Ki-ốt | Nhận diện đối tượng ưu tiên | Tuổi từ dữ liệu thẻ thuộc diện ưu tiên (dưới 6 tuổi, từ đủ 75 tuổi) → Tự động cấp dãy `UT-xxx` | Diện tự khai (thai sản, khuyết tật, người có công) → Cấp `UT-xxx` kèm cờ "chờ xác minh", điều dưỡng đối chiếu giấy tờ trước khi vào phòng |
| D13 | Web | Thêm hồ sơ người thân | Người thân từ 16 tuổi trở lên → Thêm hồ sơ bình thường, có ghi nhận căn cứ đại diện | Người thân dưới 16 tuổi → Bắt buộc xác nhận đồng ý của cha mẹ/người giám hộ trước khi lưu |

### 6.2 Scenario Matrix

| From State | To State | Rule | Action | Result |
|---|---|---|---|---|
| Đã đặt lịch web (chờ khám) | Check-in thành công | Quét QR tại ki-ốt trước giờ hẹn hoặc trễ ≤ 20 phút | Ki-ốt xác thực mã QR và tra cứu lại giá trị sử dụng thẻ | In phiếu số thứ tự đã cấp sẵn, cập nhật trạng thái "Đã có mặt" |
| Đã đặt lịch web (chờ khám) | Chuyển sang số vãng lai | Trễ > 20 phút so với giờ hẹn ghi trên phiếu | Hệ thống hủy quyền ưu tiên giờ hẹn nhưng giữ lại khoản tiền đã thanh toán | Khi quét QR tại ki-ốt, máy bảo lưu tiền khám và in ngay số thứ tự vãng lai mới (không thu tiền lần 2) |
| Đã đặt lịch web (đã thanh toán) | Chờ duyệt hoàn | Bệnh nhân bấm hủy lịch trên web trước giờ hẹn ≥ 12 tiếng | Hệ thống ghi nhận yêu cầu hủy, chuyển phòng Tài chính kế toán duyệt | Sau khi duyệt, lệnh hoàn tiền gửi ngân hàng; tiền về tài khoản trong 5–7 ngày làm việc |
| Khám vãng lai, đúng nơi ĐK ban đầu | Đã cấp số (In phiếu) | Thẻ BHYT đang có giá trị sử dụng, mã nơi ĐK trùng mã cơ sở | Bỏ qua thu tiền đầu buổi | In phiếu số thứ tự + số phòng + tầng/khu ngay lập tức |
| Khám vãng lai, khác nơi ĐK ban đầu | Đã cấp số, có phiếu chuyển điện tử | API Cổng BHXH trả về phiếu chuyển còn hiệu lực 10 ngày làm việc | Ghi mã phiếu vào hồ sơ khám | Cấp số bình thường, hồ sơ giám định ghi diện "Có phiếu chuyển" |
| Khám vãng lai, khác nơi ĐK ban đầu | Chờ quầy đối chiếu phiếu giấy | Không có phiếu điện tử nhưng bệnh nhân xác nhận có bản giấy | In phiếu dãy ưu tiên `CT-xxx` | Bệnh nhân qua quầy, nhân viên đối chiếu bản gốc và nhập mã phiếu, không xếp hàng chung |
| Khám vãng lai, khác nơi ĐK ban đầu | Đã cấp số theo diện thông cấp | Không có phiếu chuyển dưới bất kỳ dạng nào | Hiển thị quyền lợi được hưởng, ghi diện "Thông cấp" vào hồ sơ | Cấp số bình thường, **không từ chối tiếp nhận** |
| Thẻ BHYT chưa tới ngày có giá trị | Chờ thanh toán | Ngày khám sớm hơn ngày bắt đầu giá trị sử dụng ghi trên thẻ | Thông báo ngày bắt đầu được hưởng, chuyển diện thu phí | Bệnh nhân chọn đóng tiền khám dịch vụ hoặc ra quầy tư vấn |
| Khám vãng lai (Dịch vụ / Không BHYT) | Chờ thanh toán QR hoặc Tiền mặt | Phải đóng tiền công khám đầu buổi | Chọn Quét QR (đếm ngược 3 phút) hoặc chọn Tiền mặt tại quầy | Quét QR xong → ghi thời điểm thu tiền, in phiếu vào phòng khám; Chọn tiền mặt → in phiếu chờ thu ngân kích hoạt |
| Chờ thanh toán tại ki-ốt | Hủy giao dịch | Quá 3 phút không có tín hiệu tiền về từ cổng ngân hàng | Hết thời gian timeout của phiên thanh toán | Hủy giao dịch, không in phiếu, quay về màn hình chờ ban đầu |
| Đang thao tác tại ki-ốt | Tự động đăng xuất/kết thúc | Bệnh nhân rời đi, màn hình không có tương tác sau 60 giây | Timeout cảm ứng không thao tác | Xóa dữ liệu tạm trên màn hình, quay về màn hình chào đón |

### 6.3 State Transitions

```
Trạng thái Lịch hẹn Web:
[Tạm thời / Chờ thanh toán] ──(quá 10p chưa trả)──▶ [Đã hủy tự động]
            │
      (thanh toán QR xong)
            ▼
     [Đã xác nhận] ──(hủy trước 12h)──▶ [Chờ duyệt hoàn] ──(kế toán duyệt)──▶ [Đang hoàn tiền] ──▶ [Đã hoàn tiền]
            │                                   │
            │                            (kế toán từ chối)
            │                                   ▼
            │                          [Từ chối hoàn - chờ giải quyết tại quầy]
            │
            ├─(đến trễ > 20p)──▶ [Quá giờ hẹn (Bảo lưu phí, cấp số vãng lai)]
            │
   (quét QR tại ki-ốt)
            ▼
      [Đã Check-in] ──(bác sĩ gọi vào khám)──▶ [Đang khám] ──▶ [Hoàn tất]
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|---|---|---|---|---|
| Lịch hẹn | Tạm thời (Chờ thanh toán) | Đã xác nhận | Bệnh nhân chuyển khoản thành công trong 10 phút | Không |
| Lịch hẹn | Tạm thời (Chờ thanh toán) | Đã hủy tự động | Quá 10 phút không hoàn tất chuyển khoản | Không (phải đặt lịch mới) |
| Lịch hẹn | Đã xác nhận | Chờ duyệt hoàn | Bệnh nhân bấm hủy lịch trên web trước giờ hẹn ≥ 12 tiếng | Không |
| Lịch hẹn | Chờ duyệt hoàn | Đang hoàn tiền | Phòng Tài chính kế toán duyệt yêu cầu hoàn | Không |
| Lịch hẹn | Chờ duyệt hoàn | Từ chối hoàn | Kế toán từ chối (sai thông tin tài khoản, đã sử dụng dịch vụ...) | Có (bệnh nhân bổ sung thông tin tại quầy) |
| Lịch hẹn | Đã xác nhận | Quá giờ hẹn (Bảo lưu phí) | Bệnh nhân đến trễ quá 20 phút | Không (chuyển sang cấp số vãng lai, bảo lưu tiền đã đóng) |
| Lịch hẹn | Đã xác nhận | Đã Check-in | Bệnh nhân quét mã QR tại ki-ốt | Không |
| Phiếu khám | Mới tạo | Chờ xác minh phiếu chuyển | Mã nơi ĐK ban đầu khác mã cơ sở và không tra được phiếu điện tử | Có (quầy đối chiếu xong thì chuyển tiếp) |
| Phiếu khám | Mới tạo | Chờ thanh toán | Diện khám dịch vụ / không BHYT / thẻ không có giá trị sử dụng | Không |
| Phiếu khám | Chờ thanh toán | Chờ thu ngân kích hoạt | Bệnh nhân chọn "Đóng tiền mặt tại quầy" trên ki-ốt | Có (kích hoạt sau khi nộp tiền mặt) |
| Phiếu khám | Chờ thanh toán / Chờ kích hoạt / Chờ xác minh | Đã cấp số (Hợp lệ vào khám) | Thanh toán QR thành công, nộp tiền mặt tại quầy xong, hoặc diện BHYT hợp lệ | Không |
| Phiếu khám | Đã cấp số | Gọi lần 1 | Điều dưỡng/Bác sĩ bấm gọi số trên hệ thống | Có (nếu gọi lại lần 2) |
| Phiếu khám | Gọi lần 2 | Qua lượt / Hủy | Gọi 2 lần không có mặt | Không (phải vào danh sách chờ duyệt lại ở quầy) |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Đang bấm ki-ốt bị mất điện đột ngột | Dữ liệu phiên dở dang bị mất; giao dịch QR ngân hàng (nếu có) được đối soát qua mã giao dịch | Bệnh nhân di chuyển sang quầy tiếp đón để được cấp phiếu giấy dự phòng | Ki-ốt khởi động lại sẽ tự động reset về màn hình chào đón, xóa toàn bộ dữ liệu phiên |
| Đang chọn khoa thì mất kết nối mạng Internet | Dữ liệu định danh/BHYT đã đọc lưu trong bộ nhớ đệm ki-ốt ở dạng **mã hóa** | Ki-ốt chuyển tự động sang chế độ Offline, in phiếu tạm ghi "Thanh toán & xác minh tại quầy" | Khi có mạng, ki-ốt gửi gói đồng bộ lên máy chủ và **xóa bản đệm cục bộ ngay sau khi đồng bộ thành công** |
| Mất mạng đúng lúc đang tra phiếu chuyển điện tử | Mã thẻ và mã nơi ĐK ban đầu đã lấy được | Xử lý như kịch bản C2: in phiếu ưu tiên `CT-xxx` chuyển quầy đối chiếu | Nhân viên quầy tra cứu lại khi có mạng và nhập mã phiếu |
| Bệnh nhân quét QR ngân hàng bị trừ tiền nhưng ki-ốt bị kẹt giấy in | Hệ thống đã ghi nhận trạng thái thanh toán thành công và thời điểm thu tiền | Điều phối bệnh nhân sang quầy tiếp đón; nhân viên mở màn hình kiểm tra mã giao dịch và in lại phiếu | Hàng đợi in lỗi được xóa sau khi nhân viên bấm "Đã giải quyết"; hóa đơn điện tử vẫn lập theo thời điểm thu tiền |
| Đang đăng ký web thì rớt mạng / đóng trình duyệt | Đơn đặt lịch tạm lưu với thời hạn thanh toán 10 phút | Bệnh nhân mở lại web, vào mục "Lịch hẹn của tôi" để bấm thanh toán nếu còn hạn 10 phút | Sau 10 phút không thanh toán, hệ thống tự động xóa bản ghi tạm |
| Người dùng bỏ đi giữa chừng khi màn hình đang hiện thông tin cá nhân | Phiên làm việc dở dang trên ki-ốt | Không cho phép resume | Tự động xóa sạch dữ liệu trên màn hình và quay về trang chủ sau 60 giây không chạm |

### 6.5 Other Edge Cases

- **Bệnh nhân không biết chọn khoa:** Giao diện chỉ cho chọn các triệu chứng cơ bản (đau đầu, đau bụng, ho/sốt, chấn thương tay chân...). Nếu bệnh nhân phân vân, có nút bấm nổi bật: *"Tôi cần nhân viên hỗ trợ"* để gọi điều dưỡng tại sảnh.
- **Che góc nhìn & Bảo vệ dữ liệu cá nhân nhạy cảm (H5, Luật số 91/2025/QH15 và Nghị định 356/2025/NĐ-CP):**
  - Màn hình ki-ốt có tấm chắn góc nhìn hai bên (Privacy Filter) và tự động che một phần số định danh/SĐT hiển thị (`0123****8901`).
  - Phiếu in chỉ hiển thị mã số tiếp đón, số phòng và vị trí tầng/khu nhà (ví dụ: `Số: 1024 - Phòng 105 (Tầng 1 - Khu B)`), không in chữ "Phụ khoa", "Da liễu" hay "Truyền nhiễm".
  - Màn hình hàng chờ và loa gọi **chỉ phát số thứ tự, không đọc họ tên đầy đủ**.
  - Bệnh viện phải lập **hồ sơ đánh giá tác động xử lý dữ liệu cá nhân** cho hệ thống ki-ốt và web trước khi vận hành; người dùng web có đường dẫn **rút lại đồng ý**; dữ liệu đệm offline mã hóa và xóa sau đồng bộ. Lưu ý điểm giao cắt: dữ liệu khám bệnh đã vào hồ sơ bệnh án vẫn phải lưu theo quy định về hồ sơ bệnh án, không xóa theo yêu cầu rút đồng ý.
- **Người bệnh chưa có thẻ căn cước gắn chip (H3):** Ki-ốt vẫn nhận mã QR thẻ BHYT trên VssID/VNeID, mã vạch thẻ BHYT giấy cũ, hoặc nhập tay mã số BHYT; cấp số thứ tự bình thường để giảm ùn tắc, nhưng in kèm ký hiệu nhắc điều dưỡng tại cửa phòng khám đối chiếu giấy tờ tùy thân.
- **Trẻ em dưới 6 tuổi:** Chưa có thẻ căn cước nên định danh bằng mã số BHYT (hoặc giấy khai sinh tại quầy); tự động vào dãy ưu tiên `UT-xxx`.
- **Lấy số hộ người vắng mặt (H6) & chống trục lợi BHYT:** Cho phép người nhà lấy số thứ tự giữ chỗ hộ tại ki-ốt/web khi bệnh nhân đang ngồi nghỉ ngoài xe hoặc đang trên đường đến. Phiếu lấy hộ **không mở hồ sơ BHYT** — chỉ giữ chỗ. Khi vào phòng khám, bệnh nhân bắt buộc có mặt trực tiếp để điều dưỡng đối chiếu danh tính (ưu tiên so khớp sinh trắc với dữ liệu chip thẻ căn cước) trước khi hồ sơ BHYT được mở. Việc một người xử lý dữ liệu của người khác phải có căn cứ đại diện được ghi nhận trong hệ thống.
- **Bệnh nhân vắng mặt khi gọi loa:** Loa phát thanh gọi tối đa 2 lần. Nếu không có mặt, số thứ tự chuyển sang trạng thái "Qua lượt". Người nhà hoặc bệnh nhân khi quay lại phải vào quầy tiếp đón để nhân viên dời lượt chứ không được chen ngang.
- **Người bệnh thuộc danh mục bệnh hiếm, bệnh hiểm nghèo (Phụ lục I Thông tư 01/2025/TT-BYT):** Nhóm này được đến thẳng cơ sở cấp chuyên sâu, không thuộc luồng tiếp đón của ki-ốt tại bệnh viện huyện. Nếu bệnh nhân hỏi, ki-ốt chuyển sang màn hình "Gọi nhân viên hỗ trợ".

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Số định danh cá nhân (thẻ căn cước/CCCD) | Bắt buộc đúng 12 ký tự số |
| Số thẻ BHYT | Bắt buộc đúng 10 số (mã số BHXH) hoặc 15 ký tự chữ và số (thẻ BHYT mẫu cũ). Ký tự thứ 3 của mẫu 15 ký tự là mã mức hưởng — dùng để đối chiếu với kết quả tra cứu từ Cổng giám định |
| Giá trị sử dụng thẻ BHYT | Ngày khám phải nằm trong khoảng "từ ngày — đến ngày" do Cổng giám định trả về |
| Mã nơi đăng ký KCB ban đầu | Bắt buộc có trong kết quả tra cứu; thiếu trường này thì chuyển quầy xác minh |
| Phiếu chuyển cơ sở KCB | Còn hiệu lực trong 10 ngày làm việc kể từ ngày ký (Thông tư 01/2025/TT-BYT) |
| Số điện thoại (web) | Bắt buộc 10 số, bắt đầu bằng đầu số hợp lệ tại Việt Nam (đầu 03, 05, 07, 08, 09) |
| Mật khẩu tài khoản web | Tối thiểu 6 ký tự |
| Số lượng người đăng ký / phiên ki-ốt | Tối đa 4 người trong 1 phiên thao tác liên tục |
| Giới hạn đặt lịch khám trong ngày | Khám BHYT: tối đa 1 chuyên khoa ban đầu/người/ngày (khám thêm chuyên khoa thứ 2 do bác sĩ chỉ định); Khám dịch vụ: tối đa 1 lịch/ngày cùng chuyên khoa, tối đa 2 lịch/ngày khác chuyên khoa |
| Hồ sơ người thân dưới 16 tuổi | Bắt buộc có xác nhận đồng ý của cha mẹ/người giám hộ trước khi lưu |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Thời gian chờ thanh toán QR ki-ốt | 3 phút | 1 phiên thanh toán | Hủy phiên thanh toán, quay về trang chủ, không in phiếu |
| Thời gian giữ chỗ thanh toán web | 10 phút | 1 lượt đặt lịch | Tự động hủy lịch hẹn tạm, nhả lại khung giờ khám |
| Thời gian check-in trễ cho phép | 20 phút | Kể từ giờ hẹn | Hủy giờ ưu tiên, bảo lưu tiền khám đã đóng trên web và cấp số khám vãng lai mới |
| Thời hạn hủy lịch hẹn có hoàn tiền | 12 tiếng | Trước giờ hẹn khám | Từ chối hoàn tiền nếu hủy muộn hơn 12 tiếng |
| Hiệu lực phiếu chuyển cơ sở KCB | 10 ngày làm việc | Kể từ ngày ký phiếu | Quá hạn → xử lý như không có phiếu (diện thông cấp) |
| Thời gian hoàn tiền ngân hàng | 5–7 ngày làm việc | Kể từ khi kế toán duyệt yêu cầu hoàn | Tiền chuyển về đúng tài khoản đã thanh toán |
| Timeout tra cứu Cổng giám định BHYT | 10 giây | 1 lần tra cứu | Chuyển sang chế độ ngoại tuyến, in phiếu tạm xác minh tại quầy |
| Timeout màn hình ki-ốt không chạm | 60 giây | Khi đang trong phiên nhập liệu | Tự động xóa dữ liệu tạm và quay về màn hình chờ đón |
| Khóa tài khoản web do nhập sai mật khẩu | 5 lần sai liên tiếp | 15 phút | Khóa tạm thời tính năng đăng nhập trong 15 phút |
| Số lần loa gọi số thứ tự | 2 lần | Cách nhau 60 giây | Chuyển trạng thái phiếu sang "Qua lượt" |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Quá hạn thanh toán QR ki-ốt | "Giao dịch chưa hoàn tất sau 3 phút chờ. Mời cô/bác thử lại hoặc bấm chọn 'Đóng tiền mặt tại quầy' để lấy phiếu." | E-kiosk-registration-001 |
| Trễ giờ hẹn web quá 20 phút | "Lịch hẹn của cô/bác đã quá giờ hơn 20 phút. Hệ thống đã giữ lại tiền khám cô/bác đã đóng và chuyển sang cấp số thứ tự mới." | E-kiosk-registration-002 |
| Sai định dạng số định danh/BHYT | "Số thẻ hoặc số căn cước chưa đúng. Mời cô/bác kiểm tra và nhập lại, hoặc bấm nút Gọi nhân viên." | E-kiosk-registration-003 |
| Vượt quá hạn mức đặt lịch web | "Mỗi tài khoản chỉ được đặt tối đa 1 lịch/ngày cho cùng chuyên khoa (tối đa 2 lịch/ngày khác chuyên khoa)." | E-kiosk-registration-004 |
| Thẻ BHYT chưa tới ngày có giá trị sử dụng | "Thẻ bảo hiểm y tế của cô/bác bắt đầu có giá trị từ ngày {ngay_bat_dau}. Hôm nay cô/bác khám theo diện dịch vụ, hoặc mời ra quầy để được tư vấn thêm." | E-kiosk-registration-005 |
| Thẻ BHYT hết hạn hoặc tạm dừng | "Thẻ bảo hiểm y tế của cô/bác hiện không còn giá trị sử dụng. Mời cô/bác ra quầy tiếp đón để được hướng dẫn." | E-kiosk-registration-006 |
| Thông tin nhân thân trên thẻ không khớp | "Thông tin trên thẻ chưa khớp với giấy tờ. Mời cô/bác ra quầy tiếp đón để nhân viên kiểm tra giúp." | E-kiosk-registration-007 |
| Không tra cứu được phiếu chuyển điện tử | "Máy chưa tra được giấy chuyển tuyến điện tử. Nếu cô/bác có giấy chuyển bản giấy, mời bấm 'Có' để được ưu tiên tại quầy." | E-kiosk-registration-008 |

#### Success messages

| Tình huống | Wording |
|---|---|
| In số thứ tự thành công tại ki-ốt | "Đã cấp số thành công! Mời cô/bác lấy phiếu bên dưới và đến Phòng {so_phong}." |
| Nhận được phiếu chuyển điện tử | "Máy đã nhận giấy chuyển tuyến của cô/bác từ {ten_co_so}. Mời cô/bác tiếp tục chọn triệu chứng." |
| Đặt lịch trước thành công trên web | "Đặt lịch thành công! Số thứ tự của bạn là {so_thu_tu} tại Phòng {so_phong}. Vui lòng giữ mã QR này để quét tại ki-ốt khi đến viện." |
| Gửi yêu cầu hủy lịch hẹn web | "Đã ghi nhận yêu cầu hủy lịch. Bệnh viện sẽ duyệt và hoàn tiền khám về tài khoản của bạn trong 5–7 ngày làm việc kể từ khi duyệt." |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Mất kết nối mạng / lỗi cổng BHYT | "Đang mất kết nối mạng. Máy sẽ in phiếu tạm, mời cô/bác cầm phiếu ra quầy tiếp đón để hoàn tất." |
| Khám tại nơi khác nơi đăng ký ban đầu, không có phiếu chuyển | "Thẻ của cô/bác đăng ký ở {ten_noi_dang_ky}. Cô/bác vẫn được hưởng bảo hiểm khi khám tại bệnh viện này. Máy in phiếu ngay cho cô/bác." |
| Hướng dẫn sau khi in phiếu | "Mời cô/bác ngồi chờ tại khu vực Phòng {so_phong}. Hệ thống loa sẽ đọc số thứ tự khi đến lượt khám." |
| Thông báo xử lý dữ liệu tại màn hình chào | "Máy sẽ đọc thông tin thẻ của cô/bác để đăng ký khám và chỉ dùng cho việc khám bệnh. Bấm 'Đồng ý' để tiếp tục." |
| Chỉ dẫn cấp cứu tại màn hình chào | "Nếu cô/bác bị đau nặng, khó thở, chảy máu nhiều — xin đi thẳng Khoa Cấp cứu, KHÔNG cần lấy số ở máy này." |

## 8. Assumptions

- Cổng tiếp nhận dữ liệu giám định BHYT (BHXH Việt Nam) cung cấp cho cơ sở KCB chức năng tra cứu thẻ theo số định danh cá nhân hoặc mã thẻ, trả về mã nơi đăng ký KCB ban đầu, giá trị sử dụng và mức hưởng.
- BHXH Việt Nam cung cấp kênh tra cứu **phiếu chuyển cơ sở KCB điện tử** cho cơ sở tiếp nhận (giả định này quyết định tính khả thi của kịch bản C1 — xem OQ-9).
- Bệnh viện đã có HIS và đã triển khai hồ sơ bệnh án điện tử theo Thông tư 13/2025/TT-BYT, có giao diện tiếp nhận hồ sơ đăng ký từ ki-ốt và xuất XML giám định theo Quyết định 130/QĐ-BYT.
- Bệnh viện đã có phần mềm quản lý viện phí phát hành hóa đơn điện tử theo Nghị định 70/2025/NĐ-CP.
- Bảng giá dịch vụ khám bệnh của bệnh viện (do HĐND cấp tỉnh quyết theo Thông tư 21/2024/TT-BYT) được cấu hình vào hệ thống và cập nhật khi có điều chỉnh.
- Ngân hàng cung cấp giải pháp VietQR thanh toán tự động với webhook đối soát phản hồi dưới 3 giây.
- Ki-ốt được trang bị: máy in nhiệt bền bỉ; **đầu đọc chip thẻ căn cước có tem chứng nhận RAR của C06 — Bộ Công an**; đầu quét quang học 2D đọc được mã vạch thẻ BHYT giấy và mã QR trên điện thoại (VssID/VNeID, mã QR lịch hẹn).
- Phần cứng ki-ốt có tấm bảo vệ góc nhìn màn hình chống nhìn trộm (Privacy Screen Filter).
- Ki-ốt có bộ lưu điện UPS duy trì hoạt động tối thiểu 30 phút khi mất điện lưới.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|---|---|---|---|
| **Adoption:** Người cao tuổi, người dân tộc ngại dùng công nghệ, tiếp tục dồn vào quầy tiếp đón | Thường | Không đạt mục tiêu giảm tải hàng chờ, ki-ốt bị bỏ trống | Bố trí điều dưỡng hướng dẫn tận tình 1–2 tuần đầu; giao diện dùng icon cực lớn kèm giọng nói chỉ dẫn |
| **Vendor/Hạ tầng:** Mất điện lưới hoặc đứt cáp quang Internet tại vùng cao | Thường | Ki-ốt ngưng hoạt động, phát sinh ùn tắc đột ngột tại sảnh | Trang bị UPS chạy tối thiểu 30 phút; chế độ in phiếu tạm offline; chuẩn bị tệp phiếu giấy dự phòng |
| **Compliance:** Hệ thống từ chối hoặc hạ quyền lợi sai của người bệnh có thẻ đăng ký ở nơi khác (áp nhầm mô hình "trái tuyến" cũ) | Thỉnh thoảng | Người bệnh bị thu tiền sai, khiếu nại, bệnh viện bị xuất toán khi giám định | Kịch bản C3 bắt buộc: không có phiếu chuyển vẫn cấp số theo diện thông cấp; hiển thị quyền lợi trước khi in phiếu; rà lại quy tắc khi bệnh viện được xếp cấp lại |
| **Compliance:** Dữ liệu sức khỏe nhạy cảm bị lộ nơi đông người hoặc lưu trái quy định trên ki-ốt | Thỉnh thoảng | Bệnh nhân bức xúc, khiếu nại; vi phạm Luật số 91/2025/QH15 | Không in tên khoa; loa chỉ đọc số; tấm chắn góc nhìn; mã hóa và xóa bản đệm offline; lập hồ sơ đánh giá tác động trước khi vận hành |
| **Process:** Nhân viên tiếp đón lo sợ mất việc nên hướng người bệnh tránh xa ki-ốt (H7) | Thỉnh thoảng | Tỷ lệ dùng ki-ốt thấp do nhân viên cản trở ngầm | Truyền thông nội bộ rõ: ki-ốt gánh việc nhập liệu thô, nhân viên nâng vai trò thành chuyên viên điều phối, xác minh BHYT và đối chiếu phiếu chuyển |
| **Data:** Bệnh nhân nhập sai số thẻ BHYT giấy mờ rách làm chậm hàng chờ | Thường | Người phía sau phải đợi lâu, gây bực bội | Ưu tiên đọc chip thẻ căn cước và quét mã QR VssID/VNeID thay vì gõ tay; có nút gọi nhân viên hỗ trợ |
| **Vendor:** BHXH chưa mở kênh tra cứu phiếu chuyển điện tử cho cơ sở tiếp nhận | Thỉnh thoảng | Kịch bản C1 không chạy được, mọi ca khác nơi đăng ký dồn về quầy | Thiết kế C2 làm đường lui mặc định; xác nhận với BHXH tỉnh trước khi chốt phạm vi (OQ-9) |

## 10. Success Criteria (preliminary)

- Giảm tối thiểu 40% số lượt bệnh nhân phải xếp hàng lấy số tại quầy tiếp đón tập trung.
- Thời gian trung bình để 1 bệnh nhân hoàn tất lấy số và thanh toán tại ki-ốt dưới 90 giây.
- Tỷ lệ giao dịch thanh toán QR và in số thành công đạt trên 90% (không bao gồm sự cố mất điện).
- Tỷ lệ bệnh nhân đặt lịch trước qua web check-in đúng hẹn đạt trên 30% sau 3 tháng triển khai.
- Không phát sinh trường hợp người bệnh bị từ chối cấp số hoặc bị thu sai tiền do áp nhầm quy định về nơi đăng ký KCB ban đầu.

## 11. Open Questions

- [ ] OQ-1: Màn hình thao tác riêng của Nhân viên tiếp đón bao gồm những chức năng nghiệp vụ chi tiết nào (ngoài việc duyệt danh sách và in lại phiếu lỗi)?
- [ ] OQ-2: Quy tắc xếp lượt khám khi bệnh nhân bị "Qua lượt" (do vắng mặt khi loa gọi 2 lần) được nhân viên tiếp nhận lại sẽ ưu tiên xếp sau bao nhiêu ca?
- [ ] OQ-3: Danh mục các nhóm triệu chứng hình ảnh trực quan cần được Hội đồng Y khoa của bệnh viện rà soát và phê duyệt chuẩn hóa như thế nào để phù hợp nhất với nhận thức của đồng bào vùng cao?
- [ ] OQ-4: Khảo sát đo lường chính xác lượng bệnh nhân dồn ứ vào khung giờ đỉnh điểm (7h00 - 8h30 sáng) để tính toán thời điểm đề xuất bệnh viện đầu tư thêm ki-ốt thứ 2.
- [ ] OQ-5: Bệnh viện được xếp cấp chuyên môn kỹ thuật nào và đạt bao nhiêu điểm? Kết quả này quyết định mức hưởng BHYT ngoại trú áp dụng tại cơ sở, đặc biệt sau mốc 01/7/2026.
- [ ] OQ-6: Mức tham chiếu đang áp dụng tại thời điểm triển khai là bao nhiêu, để tính đúng ngưỡng miễn cùng chi trả?
- [ ] OQ-7: Bệnh viện đang dùng HIS nào, đã hoàn tất hồ sơ bệnh án điện tử theo Thông tư 13/2025/TT-BYT chưa, và có sẵn giao diện tiếp nhận hồ sơ đăng ký từ ki-ốt không?
- [ ] OQ-8: Quy trình phát hành hóa đơn điện tử hiện tại khi thu tiền khám là xuất ngay từng lượt hay tổng hợp cuối ngày?
- [ ] OQ-9: BHXH có cung cấp kênh tra cứu phiếu chuyển cơ sở KCB điện tử cho cơ sở tiếp nhận không, qua kênh nào và cần thủ tục gì? (quyết định tính khả thi của kịch bản C1)
- [ ] OQ-10: Tỷ trọng bệnh nhân đến từ trạm y tế xã có phiếu chuyển, và tỷ trọng bệnh nhân tái khám theo giấy hẹn, chiếm bao nhiêu phần trăm lượt khám mỗi sáng?
- [ ] OQ-11: Ai là người duyệt lệnh hoàn tiền tại phòng Tài chính kế toán và thời hạn duyệt nội bộ là bao lâu?

## 12. Next Steps

Sau khi BA và các bên liên quan review bản Brainstorm này:
- `/urd kiosk-registration` — Làm rõ chân dung người dùng, hành trình chi tiết (User Journey) và các yêu cầu người dùng.
- `/brd kiosk-registration` — Xây dựng Business Case, tính toán hiệu quả đầu tư và các mục tiêu kinh doanh/vận hành cấp bệnh viện.
- `/srs kiosk-registration` — Đặc tả yêu cầu phần mềm chi tiết (FR, NFR, Data Dictionary, Error Matrix).
