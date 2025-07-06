import pandas as pd

# 文件路径
original_file = 'origin.xlsx'
compare_file = 'compare.xlsx'
output_file = 'name_id_mismatch.xlsx'

# 读取 Excel 所有 sheet
origin_excel = pd.read_excel(original_file, sheet_name=None, engine='openpyxl')
compare_excel = pd.read_excel(compare_file, sheet_name=None, engine='openpyxl')

# 存储所有不一致记录
mismatch_rows = []

# ✅ 统一格式处理函数（处理 .0 问题）
def clean_id(val):
    try:
        return str(int(float(val)))
    except:
        return ''

# 遍历 compare 中每个 sheet
for compare_sheet, df_comp in compare_excel.items():
    df_comp.columns = df_comp.columns.astype(str).str.strip()

    if '姓名' not in df_comp.columns or '学号' not in df_comp.columns:
        continue

    df_comp['姓名'] = df_comp['姓名'].astype(str).str.strip()
    df_comp['学号'] = df_comp['学号'].apply(clean_id)

    for _, row in df_comp.iterrows():
        name = row['姓名']
        id_cmp = row['学号']
        found = False

        # 在 origin 的所有 sheet 中查找该姓名
        for origin_sheet, df_orig in origin_excel.items():
            df_orig.columns = df_orig.columns.astype(str).str.strip()

            if '姓名' not in df_orig.columns or '学号' not in df_orig.columns:
                continue

            df_orig['姓名'] = df_orig['姓名'].astype(str).str.strip()
            df_orig['学号'] = df_orig['学号'].apply(clean_id)

            matched = df_orig[df_orig['姓名'] == name]
            if not matched.empty:
                found = True
                id_orig = matched.iloc[0]['学号']
                if id_orig != id_cmp:
                    mismatch_rows.append({
                        '姓名': name,
                        'compare学号': id_cmp,
                        'origin学号': id_orig,
                        'compare_sheet': compare_sheet,
                        'origin_sheet': origin_sheet
                    })
                break  # 找到后就不再继续查其他 sheet

        # 也可以记录 compare 中有但 origin 中找不到的姓名（可选功能）
        # if not found:
        #     mismatch_rows.append({
        #         '姓名': name,
        #         'compare学号': id_cmp,
        #         'origin学号': '未找到',
        #         'compare_sheet': compare_sheet,
        #         'origin_sheet': '无'
        #     })

# 写入结果文件
if mismatch_rows:
    df_output = pd.DataFrame(mismatch_rows)
    df_output.to_excel(output_file, index=False)
    print(f"✅ 共发现 {len(df_output)} 条学号不一致，已写入文件：{output_file}")
else:
    print("✅ 所有 compare 中的姓名学号均与 origin 匹配，无差异。")
