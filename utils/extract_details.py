def extract_comments_details(soup):
    comments_segment = soup.find_all('ytd-comment-thread-renderer')
    comments = []
    for comment in comments_segment:
        user_info = comment.find('ytd-comment-renderer').find('a', {'id': 'author-text'})
        user_name = user_info.text.strip()
        comment_text = comment.find('yt-formatted-string', {'id': 'content-text'}).text.strip()
        likes = comment.find('span', {'id': 'vote-count-middle'}).text.strip()
        comment_time = comment.find('a', {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).text.strip()
        thumbmail_url_tag = comment.find('yt-img-shadow', {"class": "style-scope ytd-comment-renderer no-transition"})
        if thumbmail_url_tag is not None:
            thumbmail_url = thumbmail_url_tag.find('img').get('src')
        else:
            thumbmail_url = None
        comments.append([user_name, comment_text, comment_time, likes, thumbmail_url])

    return comments
