import pandas as pd

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, columnnames)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = self.df[self.df[columnnames] == columnnames ].index
        df = self.df.drop(unwanted_rows , inplace=True)
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df = self.df.drop_duplicates()

        
        return df
    
    def convert_to_datetime(self, columns)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df[columns]= pd.to_datetime(self.df[columns])
        
        
        return self.df
    
    def convert_to_numbers(self, columns)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df[columns] = pd.to_numeric(self.df[columns])
#         """
#         convert columns like polarity, subjectivity, retweet_count
#         favorite_count etc to numbers
#         """
        
        return self.df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
            for i in range(len(self.df)):
                if self.df.language[i] !='eng':
                    df = self.df.drop(i)
                
        return df