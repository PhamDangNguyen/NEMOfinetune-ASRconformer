import json

input_file_path = "/home/pdnguyen/fast_confomer_finetun/NEMOfinetune-ASRconformer/Train/metadata_train/testcv.json"
output_file_path = "/home/pdnguyen/fast_confomer_finetun/NEMOfinetune-ASRconformer/Train/metadata_tokenizer/teranscrip_all.json"

with open(input_file_path, "r", encoding="utf-8") as input_file, \
     open(output_file_path, "w", encoding="utf-8") as output_file:

    for line in input_file:
        data = json.loads(line)
        text = data.get("text", "")
        cleaned_text = text.replace('"', '')
        # Tạo một từ điển mới chứa trường "text" và ghi vào tệp JSON mới
        output_file.write(cleaned_text + "\n")
