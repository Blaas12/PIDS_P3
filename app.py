from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/data/lote_inicial', methods=['GET'])
def get_data():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lote_inicial")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/data/precios', methods=['GET'])
def get_data_precios():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Precios")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/data/trayectos_patinete', methods=['GET'])
def get_data_trayectos_patinete():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Número_de_Trayectos")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/data/trayectos_totales', methods=['GET'])
def get_data_trayectos_totales():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Número_total_de_Trayectos")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/data/patinetes_totales', methods=['GET'])
def get_data_patinetes_totales():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Número_total_de_Patinetes")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/data/resumen', methods=['GET'])
def get_data_resumen():
    try:
        conn = psycopg2.connect(
            database="patinetes",
            user="postgres",
            password="aaa",
            host="proyecto_3-postgresql_contenedor-1",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Resumen")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
