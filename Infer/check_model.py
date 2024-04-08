import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecHybridRNNTCTCBPEModel.from_pretrained(model_name="nvidia/stt_en_fastconformer_hybrid_large_streaming_multi")

# Optional: change the default latency. Default latency is 1040ms. Supported latencies: {0: 0ms, 1: 80ms, 16: 480ms, 33: 1040ms}.
# Note: These are the worst latency and average latency would be half of these numbers.
asr_model.encoder.set_default_att_context_size([70,13]) 

#Optional: change the default decoder. Default decoder is Transducer (RNNT). Supported decoders: {ctc, rnnt}.
asr_model.change_decoding_strategy(decoder_type='rnnt')

a = asr_model.transcribe(['2086-149220-0033.wav'])
print(a[0])