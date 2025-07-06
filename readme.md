# 🎓 Excel 学号一致性检查工具

本项目是一个用于比对两个 Excel 文件中学生姓名与学号是否一致的 Python 脚本工具，支持多 Sheet、格式混乱、学号中带 `.0` 的情况等，适用于大规模学生信息核对。

---

## 📌 功能简介

- 遍历 `compare.xlsx` 中每一个 Sheet，逐行读取“姓名”和“学号”；
- 在 `origin.xlsx` 的所有 Sheet 中查找对应“姓名”；
- 若找到，比较学号是否一致；
- 自动处理 Excel 导致的 `.0` 问题（如 `20230001.0` 与 `20230001`）；
- 如果不一致，记录并输出为新的 Excel 文件 `name_id_mismatch.xlsx`。

---

## 📂 文件结构示例

- `origin.xlsx`: 原始完整学生信息表，可能包含多个 sheet，列如 `姓名`、`学号`、`导师` 等。
- `compare.xlsx`: 需要检查的对比表，多个 sheet，包含 `姓名` 和 `学号`。
- `diff_excel.py`: 脚本主体。
- `name_id_mismatch.xlsx`: 脚本运行后输出的差异结果。

---

## 🚀 快速开始

### 1. 安装依赖

确保 Python 版本 ≥ 3.7，安装所需库：

```bash
pip install pandas openpyxl
```

```bash
pip install pandas openpyxl