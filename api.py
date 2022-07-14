from config import *



@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'data': Movies.get_movies()})



@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return jsonify({'data': Movies.get_movie_by_id(id)})



@app.route('/movies', methods=['POST'])
def add_movie():

    request_data = request.get_json()  
    Movies.save_movie(request_data["title"], request_data["year"],request_data["genre"])
    return jsonify({})


@app.route('/movies/<int:id>', methods=['PUT'])
def update_movies(id):
    request_data = request.get_json()
    Movies.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("Movie Updated", status=200, mimetype='application/json')
    return response


@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):

    Movies.delete_movie(id)
    return jsonify({'data': Movies.delete_movie(id)})


if __name__ == "__main__":
    app.run(port=8000, debug=True)

