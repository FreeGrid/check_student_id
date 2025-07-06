# 🎓 Excel 学号核对工具

本工具用于对比两个 Excel 文件中的姓名与学号是否一致，适用于核查是否有学号填写错误、录入错位等情况。特别适合班级名单、学籍系统导出、教务数据核查等场景。

---

## 🗂️ 功能说明

- 支持对比两个 Excel 文件中多个 Sheet 的数据；
- 自动匹配姓名并比较学号是否一致；
- 自动处理 Excel 中常见的 `.0` 问题（如 `20230001.0`）；
- 支持跳过列名不规范或缺失的 Sheet；
- 输出所有姓名匹配但学号不一致的记录；
- 忽略空值或非规范数据，结果鲁棒可靠。

---

## 📄 输入文件格式

你需要准备两个 Excel 文件：

### 1. `origin.xlsx`（原始数据）

- 可以包含多个 Sheet，每个 Sheet 是一个班级或分组；
- 至少包含以下两列：
  - `姓名`
  - `学号`
- 其他列（如手机号、导师、备注等）可以存在但不参与对比。

### 2. `compare.xlsx`（需要比对的数据）

- 同样可以包含多个 Sheet；
- 每个 Sheet 至少包含：
  - `姓名`
  - `学号`

📌 **注意**：Sheet 名不需要一致，工具会自动在所有 Sheet 中查找匹配项。

---

## 🧪 示例数据结构

| 姓名 | 学号     |
| ---- | -------- |
| 张三 | 20230001 |
| 李四 | 20230022 |

---

## 🖥️ 使用方法

### 1. 安装依赖

建议在虚拟环境中运行：

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows

pip install pandas openpyxl
```

------

### 2. 放置文件

将以下文件放在项目根目录：

- `origin.xlsx`
- `compare.xlsx`
- `diff_excel.py`（比对脚本）

------

### 3. 运行脚本

```bash
python diff_excel.py
```

运行成功后，如果存在不一致，将看到如下提示：

```bash
✅ 共发现 3 条学号不一致，已写入文件：name_id_mismatch.xlsx
```

否则：

```bash
✅ 所有 compare 中的姓名学号均与 origin 匹配，无差异。
```

------

## 📤 输出结果格式

生成的 `name_id_mismatch.xlsx` 包含以下列：

| 姓名 | compare学号 | origin学号 | compare_sheet | origin_sheet |
| ---- | ----------- | ---------- | ------------- | ------------ |
| 张三 | 20230002    | 20230001   | 第二组        | 班级A        |

------

## 🔒 数据规范建议

为获得更准确的结果，请注意：

- 学号应尽量为整数（20230001），避免带 `.0` 的格式；
- 姓名不应含有空格或其他无关字符；
- 表头字段务必包含 `姓名` 和 `学号`，否则该 Sheet 会被跳过。

------

## 📦 项目结构

```text
your_project/
├── compare.xlsx
├── origin.xlsx
├── diff_excel.py
├── name_id_mismatch.xlsx  # （运行后自动生成）
└── README.md
```

