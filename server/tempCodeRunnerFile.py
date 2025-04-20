import pickle, json, os, numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft,bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except: 
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model  # Add this line to modify __model globally

    try:
        # Ensure correct path for 'columns.json'
        json_path = os.path.join(os.path.dirname(__file__), "artifacts", "columns.json")
        with open(json_path, 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __location = __data_columns[3:]

        global __model
        # Ensure correct path for model file
        model_path = os.path.join(os.path.dirname(__file__), "artifacts", "Bengaluru_house_data_model.pickle")
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)

        print("loading saved artifacts...done")
    except Exception as e:
        print(f"Error loading artifacts: {e}")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 2000, 2, 3))
    print(get_estimated_price('Kalhalli', 2000, 2, 3)) #other location