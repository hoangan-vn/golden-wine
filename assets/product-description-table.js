// Map all possible fields you want to display in order
const fields = [
  "Xuất xứ",
  "Quốc gia",
  "Thương hiệu",
  "Vùng",
  "Vùng nho",
  "Nhà sản xuất",
  "Phân loại",
  "Loại vang",
  "Giống nho",
  "Nồng độ",
  "Hương vị",
  "Thức ăn",
  "Dung tích",
  "Tuổi rượu",
  "Phân loại rượu",
  "Thể tích",
  "Phân cấp",
  "Hộp đi kèm",
  "Nồng độ cồn",
  "Tỉ lệ đánh bóng gạo",
];

function formatDescription(description) {
  // Turn product description string into an object
  const data = {};
  description.split(/(?=\b[A-ZÀ-ỹ][^:]+:)/g).forEach(part => {
    const [key, ...rest] = part.split(":");
    if (key && rest.length > 0) {
      data[key.trim()] = rest.join(":").trim();
    }
  });

  // Build HTML table including missing fields as blank
  let html = '<table style="width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: 15px;">';
  fields.forEach(field => {
    html += `
      <tr>
        <td style="padding: 8px; font-weight: bold;">${field}</td>
        <td style="padding: 8px;">${data[field] || ""}</td>
      </tr>
    `;
  });
  html += "</table>";
  return html;
}

