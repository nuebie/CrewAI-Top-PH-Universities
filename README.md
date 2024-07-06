# Project Setup

1. **Install a LLM locally from Ollama**
   - Follow the instructions provided by Ollama to install a Language Learning Model (LLM) on your local machine.

2. **Obtain an API Key from Serper**
   - Sign up on the Serper platform and generate an API key.

3. **Create a .env file**
   - In the root directory of your project, create a file named `.env`.
   - Add the following content to the `.env` file:
     ```
     MODEL=your_llm_name
     SERPER_API_KEY=your_serper_api_key
     ```
     Replace `your_llm_name` with the name of the LLM you installed and `your_serper_api_key` with the API key you obtained from Serper.

4. **Install the packages in the requirements.txt**
   - Run the following command to install the required packages:
     ```sh
     pip install -r requirements.txt
     ```

5. **Run the main.py file**
   - Execute the following command to run the project:
     ```sh
     python main.py
     ```

Make sure to follow each step carefully to ensure that the project is set up correctly.
