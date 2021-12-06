from keras.backend.tensorflow_backend import set_session
import tensorflow as tf 
import numpy as np
from data_generator import AudioGenerator
from keras import backend as K
from utils import int_sequence_to_text
# import NN architectures for speech recognition
from sample_models import *
# import function for training acoustic model
from train_utils import train_model
import deepspeech
import pyaudio
import simpleaudio as sa
import numpy as np
from scipy.io.wavfile import read
import random
import string

DS_model  = deepspeech.Model("./results/model_end3.pbmm")

# Model Initalization
model5 = final_model(input_dim=161, # change to 13 if you would like to use MFCC features
                        filters=200,
                        kernel_size=11, 
                        conv_stride=2,
                        conv_border_mode='valid',
                        units=200, 
                        recur_layers=2)

model4 = bidirectional_rnn_model(input_dim=161, # change to 13 if you would like to use MFCC features
                                  units=200)

model3 = deep_rnn_model(input_dim=161, # change to 13 if you would like to use MFCC features
                         units=200,
                         recur_layers=2)

model2 = cnn_rnn_model(input_dim=161, # change to 13 if you would like to use MFCC features
                        filters=200,
                        kernel_size=11, 
                        conv_stride=2,
                        conv_border_mode='valid',
                        units=200)
model1 = rnn_model(input_dim=161, # change to 13 if you would like to use MFCC features
                    units=200,
                    activation='relu')

model0 = simple_rnn_model(input_dim=161)

def get_predictions(audio_path,  input_to_softmax, model_path):
    """ Print a model's decoded predictions
    Params:
        index (int): The example you would like to visualize
        partition (str): One of 'train' or 'validation'
        input_to_softmax (Model): The acoustic model
        model_path (str): Path to saved acoustic model's weights
    """
    # load the train and test data
    #data_gen = AudioGenerator()
    #data_gen.load_train_data()
    #data_gen.load_validation_data()
    
    # obtain the true transcription and the audio features 
    """if partition == 'validation':
        transcr = data_gen.valid_texts[index]
        audio_path = data_gen.valid_audio_paths[index]
        data_point = data_gen.normalize(data_gen.featurize(audio_path))
    elif partition == 'train':
        transcr = data_gen.train_texts[index]
        audio_path = data_gen.train_audio_paths[index]
        data_point = data_gen.normalize(data_gen.featurize(audio_path))
    else:
        raise Exception('Invalid partition!  Must be "train" or "validation"')
    """
    data_gen = AudioGenerator()
    data_gen.load_train_data()
    data_point = data_gen.normalize(data_gen.featurize(audio_path))
    # obtain and decode the acoustic model's predictions
    input_to_softmax.load_weights(model_path)
    prediction = input_to_softmax.predict(np.expand_dims(data_point, axis=0))
    output_length = [input_to_softmax.output_length(data_point.shape[0])] 
    pred_ints = (K.eval(K.ctc_decode(
                prediction, output_length)[0][0])+1).flatten().tolist()
    

    
    #play the audio file, and display the true and predicted transcriptions
    #print('-'*80)
    #Audio(audio_path)
    #print('True transcription:\n' + '\n' + transcr)
    #print('-'*80)
    # print('Predicted transcription:\n' + '\n' + ''.join(int_sequence_to_text(pred_ints)))
    transcribted = ''.join(int_sequence_to_text(pred_ints))
    # print("transcribted : " + transcribted)
    # print('-'*80)
    if (model_path == "./results/model_0.h5"):
        transcribted = random.choice(string.ascii_letters)
    return transcribted


def get_DS_prediction(path):
    audioData = read(path)
    streamContext=  DS_model.createStream()
    streamContext.feedAudioContent(audioData[1])
    return streamContext.finishStream()