# Hướng dẫn train model conformer ASR của nemo
## Tạo Vocab và Tokenizer dựa trên transcript của tập train
Chạy file ```prepare_data.sh``` cùng với tham số đã được chỉnh trong đó => xuất ra một output tại thư mục dict_N gồm:
- tokenizer.model
- tokenizer.vocab
- vocab.txt
## Tạo định dạng metadata để train
- Ví dụ: metadata sau tiền xử lý bộ bud500 đang có dạng
```
[
    {
        "name": "/home/pdnguyen/VietAIbud500/Bud500_convert/valid/wavs/0.wav",
        "duration": 1.71175,
        "transcript": "câu chuyện cổ tích này mà thôi"
    },
    
    .
    .
    .
    {
        "name": "/home/pdnguyen/VietAIbud500/Bud500_convert/valid/wavs/1.wav",
        "duration": 2.359375,
        "transcript": "lắm mà nhà ba mẹ em cũng nhiều phòng lắm"
    }
]
```
- Xử lý lại bằng hàm ```function_N/convert_json2train.py``` để thu được dạng chuẩn mainfest đưa vào train và valid như sau:
```
{"audio_filepath": "/home/pdnguyen/VietAIbud500/Bud500_convert/test/wavs/0.wav", "duration": 3.0018125, "text": "tôi thì tôi nghĩ rằng là hầu hết tất cả"}
    .
    .
    .
{"audio_filepath": "/home/pdnguyen/VietAIbud500/Bud500_convert/test/wavs/1.wav", "duration": 2.4616875, "text": "khách du lịch quốc tế và trong nước bốn"}
```
* NOTE: Cần dữ liệu đi kèm metadata
## Training model
Chạy file ```train.sh``` để truyền các tham số vào ```speech_to_text_hybrid_rnnt_ctc_bpe.py``` để train