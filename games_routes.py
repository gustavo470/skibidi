from flask import Blueprint, request, jsonify
from controllers.games_controller import (
    create_game,
    get_all_games,
    get_game_by_id,
    update_game,
    delete_game
)

game_bp = Blueprint('game_bp', __name__)

# POST - Criar jogo
@game_bp.route('/games', methods=['POST'])
def add_game():
    data = request.get_json()
    result, status = create_game(data)
    return jsonify(result), status


# GET - Listar todos os jogos
@game_bp.route('/games', methods=['GET'])
def list_games():
    result, status = get_all_games()
    return jsonify(result), status


# GET - Buscar jogo por ID
@game_bp.route('/games/<int:id>', methods=['GET'])
def get_game(id):
    result, status = get_game_by_id(id)
    return jsonify(result), status


# PUT - Atualizar jogo por ID
@game_bp.route('/games/<int:id>', methods=['PUT'])
def update_game_route(id):
    data = request.get_json()
    result, status = update_game(id, data)
    return jsonify(result), status


# DELETE - Excluir jogo por ID
@game_bp.route('/games/<int:id>', methods=['DELETE'])
def delete_game_route(id):
    result, status = delete_game(id)
    return jsonify(result), status
