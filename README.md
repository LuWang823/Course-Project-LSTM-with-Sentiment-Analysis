#Yahoo Stock Prediction through Time Series and Sentiment Analyses of News: Apple Inc. 

**DSCI 521 Data Analysis and Interpretation, Team Project Presentation**
Winter Term 2023, Instructor: Dr. Xiaohua Tony Hu
Group Members: Wang,Lu; Rekha,Anamika; Pai,Srinivas; Pan,Kenneth; Kumar,Divyanshu 

**Introduction**:

We all know how Coca-Cola's stock value came crashing down when Ronaldo rejected it publicly. Due to several macro and micro aspects, including politics, international economic conditions, unforeseen occurrences, a company's financial performance, and others, accurate stock price forecast is exceedingly difficult. These factors make it a point for the researchers, data analysts, and data scientists of the companies to study and discover the patterns in the data which will help in boosting the financial status of the organization. We are trying to take in account the other variables such as news that play a major role in stock market.  

Our project is an attempt to predict the stock market using not only the stock data, but also sentiment analysis predicted according to the news. Sentiment analysis is to investigate the emotions expressed by individuals about a product, a service, a brand or more generally a subject. It will provide valuable information of how news could influence stock prices. Specifically, we will apply sentiment analysis of news and time series analysis to predict the closing price of Apple stock recorded by Yahoo finance.
**Datasets**: [Yahoo stock prediction by news] (https://www.kaggle.com/datasets/deepakjoshi2k/yahoo-stock-prediction-by-news) 

**Models**: 

We used [`Natural Language Toolkit`] (https://www.nltk.org) for sentiment analysis of news and applied `Long Short-Term Memory (LSTM)` neural network for the time series analysis.

NLTK is a leading language processing toolkit of Python. It provides easy-to-use interfaces to [over 50 corpora and lexical resources] (https://www.nltk.org/nltk_data/) such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. 

LSTM (Long Short-Term Memory) is a type of neural network architecture that is commonly used in deep learning for tasks that involve sequential data, such as speech recognition, natural language processing, and time-series prediction. It was introduced by Hochreiter and Schmidhuber in 1997.
The main advantage of LSTM over traditional `recurrent neural networks (RNNs)` is its ability to handle the vanishing gradient problem, which occurs when the gradients become too small during training and the model is unable to learn from the data. LSTMs use a gating mechanism to selectively forget or remember information from the previous time step, which allows them to maintain long-term dependencies in the data and avoid the vanishing gradient problem. This is realized through the three gates of each cell: an input gate, a forget gate, and an output gate. The input gate controls the amount of new information that is added to the cell, while the forget gate controls the amount of old information that is removed from the cell. The output gate controls the amount of information that is passed to the next time step. [`More details of RNN and LSTM`] (https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks)
We compared models with and without sentiment analysis.

**Target Audience**:

The target audience for stock market prediction can include investors that are interested in the stock market, traders, financial analysts, Data science students/researchers, and the general public. 
- **Investors and traders** may use stock market sentiment analysis to make their own decisions on whether they want to buy or sell shares of the company. The analysis involves current and historic data along with emphasis on sentimental analysis to calculate and predict the effect of news on the product, which are a key factor in the decision for long-term as well as short term investments. For example, if the sentiment analysis of the news shows a positive output for Apple, investors might consider buying the stock. The analysis will help the potential traders to know better about their entry and exit points. This will prevent them from entering and exiting the market at the wrong time and avoids capital fail on full potential of making profits.
- **Financial analysts** could examine and evaluate consumer behaviors towards the company products, strategic initiatives, and so on. 
- **Data science students and researchers** could also be a target audience, as they might gain a deeper understanding of using machine learning models to predict the stock market. They can identify and study the trading signals and catches the patterns of the stock market's movement by analyzing quantifiable data from actions on the stock market, such as stock prices, historical returns, transaction volume and consumer behaviors. 
- **The general public** is similar to investors, but for people who are not familiar with the stock market might use this analysis to learn about how news articles can impact the performance of a company’s stock.


**Challenges and Limitations**:

- **The source of data is insufficient.** Other sources of news could also influence the stock price.
- **The time spans of analysis remain to be further investigated.** For LSTM model, we used the previous day to predict next day’s stock price. However, the time spans could be extended to weeks, months, or even years. Future work could conduct more experiments with different settings. 
- **The impact factors of stock prices are complex.** Other factors such as economic indicators, company financials, and market sentiment could also play a role in stock price movements. 





