
from flask import Flask, request, jsonify, render_template
import shorttext


app = Flask(__name__)
w2v_model = shorttext.utils.load_word2vec_model('test_w2v_model.bin', binary=True)


@app.route('/wordvector',methods=['POST'])
def wordvector():
    data = request.get_json(force=True)
    word = data['word']
    vector = w2v_model[word]
    return jsonify({'vector': vector.tolist()})


@app.route('/mostsimilarvector',methods=['POST'])
def mostsimilarword():
    data = request.get_json(force=True)
    pos1 = data['pos1']
    pos2 = data['pos2']
    neg = data['neg']
    theword = w2v_model.most_similar([pos1, pos2], [neg])
    return jsonify(theword)


@app.route('/vectorsize',methods=['POST'])
def vectorsize():
    vecsize = w2v_model.vector_size
    return jsonify({'vectorsize': vecsize})


if __name__ == "__main__":
    app.run(debug=True)