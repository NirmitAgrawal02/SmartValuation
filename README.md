# SmartValuation
Building a full stack web application that integrates a simple machine learning model to predict housing prices based on user input

## Features

- **User Interface**: A styled form to input house details and select a machine learning model.

- **Machine Learning Models**: Choose between Linear Regression, Random Forest Regression, or Support Vector Regression (SVR).

- **Backend**: REST API to process predictions and store results.

- **Database**: SQLite to log each prediction request.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8+**: Required for the backend and model training.

- **Node.js 16+ and npm**: Required for the Next.js frontend.

- **Git**: To clone the repository (optional).

## How to Run Locally

Follow these steps to set up and run the application on your local machine.


### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/SmartValuation.git
cd SmartValuation
```

### Step 2: Set Up the Backend

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the backend server:
    ```bash
    python app.py
    ```

    The backend will be available at `http://127.0.0.1:5000`.

### Step 3: Set Up the Frontend

1. Navigate to the `frontend` directory:
    ```bash
    cd ../frontend
    ```

2. Install the required Node.js packages:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm run dev
    ```

    The frontend will be available at `http://localhost:3000`.

### Step 4: Access the Application

Open your browser and navigate to `http://localhost:3000` to use the application.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [your-email@example.com].