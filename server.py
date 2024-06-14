from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/data', methods=['GET'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400
    
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    if temperature and humidity:
        print(f"Received temperature: {temperature}°C, humidity: {humidity}%")
        return jsonify({'status': 'success', 'temperature': temperature, 'humidity': humidity}), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)