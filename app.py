# Import necessary libraries and functions
from flask import Flask, render_template, request
from textblob import TextBlob 
# from ai import need_model
from opean import get_openai_response

# model = need_model()

# Creating a Flask app
app = Flask(__name__)

# Render the index.html template when accessing the root route
@app.route('/filterblog')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate():
    return render_template('generate.html')

 
# Handle form submission and render the result.html template with sentiment analysis result
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        filter=request.form['filter']
        print(type(filter))
        # response=model.generate_content("Check what is vulgar word in this content after that provide reframe content without vulgar content from "+text)
        # blob = TextBlob(text)
        # sentiment = blob.sentiment
        response=get_openai_response(text,filter)

        
        
        # Render the result.html template with sentiment analysis results
        return render_template('result.html', 
                               content=response, 
                               filter=filter
                            #    polarity=sentiment.polarity, 
                            #    subjectivity=sentiment.subjectivity
                               )
 
        
# Driver function
if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5080)
