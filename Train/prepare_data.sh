python /home/pdnguyen/fast_confomer_finetun/NEMOfinetune-ASRconformer/Train/process_asr_text_tokenizer.py \
        --data_file="/home/pdnguyen/fast_confomer_finetun/NEMOfinetune-ASRconformer/Train/metadata/traincv.json" \
        --data_root="/home/pdnguyen/fast_confomer_finetun/NEMOfinetune-ASRconformer/Train/dict_N" \
        --vocab_size=20000 \
        --tokenizer="spe" \
        --no_lower_case \
        --spe_type="bpe" \
        --spe_character_coverage=1.0 \
        --log
