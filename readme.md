## Movies and Friends
Rate and Review movies among friends

### Setup
1. pip install -r requirements.py
2. ./manage.py migrate
3. ./manage.py runserver

### Examples

#### List movies in database

curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: 2ef0b51f-a9fe-e91a-f041-95aeed8d473d" "http://127.0.0.1:8000/movies/"

[
  {
    "name": "doctor strange",
    "id": 1
  },
  {
    "name": "kodi",
    "id": 2
  },
  {
    "name": "kashmora",
    "id": 3
  }
]

#### Post movie into database

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Cache-Control: no-cache" -H "Postman-Token: 7ff99554-779d-3f88-b2d8-30347206810d" -d 'name=mission impossible' "http://127.0.0.1:8000/movies/"

{
  "name": "mission impossible",
  "id": 4
}

#### View Movie Reviews

curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: b9e79967-7530-06d5-f15c-d134aaca8707" "http://127.0.0.1:8000/movies/1/ratings/"

[
  {
    "rating": 1,
    "id": 1,
    "movie": "doctor strange"
  },
  {
    "rating": 2,
    "id": 2,
    "movie": "doctor strange"
  }
]

#### Post Movie Review

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Cache-Control: no-cache" -H "Postman-Token: 515e8229-256e-d46c-9d10-11739361ad9f" -d 'rating=4&movie=2' "http://127.0.0.1:8000/ratings/"

{
  "rating": 1,
  "movie": 5
}