import pandas as pd
import numpy as np

def find_similar_books(books, book_id, dot_prod_book_genres):
    book_index = np.where(books['bookID'] == book_id)[0][0]

    similar_indices = np.where(dot_prod_book_genres[book_index] >= 1)[0]

    similar_books = np.array(books.iloc[similar_indices, ]['title'])

    return similar_books

def get_books_title(books, book_ids):
    books_list = list(books[books['bookID'].isin(book_ids)]['title'])
    return books_list

def recommend_books(user, books):
    user = pd.read_json(user)
    books = pd.read_json(books)
       
    books_temp = np.array(user['bookID'])
    books_title = np.array(get_books_title(books, books_temp))
        
    book_genres = np.array(books.iloc[:,10:])
    dot_prod_book_genres = book_genres.dot(np.transpose(book_genres))

    recommendations = np.array([])
    for book in books_temp:
        recommended_books = find_similar_books(books, book, dot_prod_book_genres)
        temp_recommendations = np.setdiff1d(recommended_books, books_title)
        recommendations = list(temp_recommendations)
    
    recommended = books.loc[books['title'].isin(recommendations)]
    recommended = recommended[recommended['published'] == 1]

    return recommended['bookID'].sample(n=7).to_json(orient='records')