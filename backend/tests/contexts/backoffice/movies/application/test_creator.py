from src.contexts.backoffice.movies.application.movie_creator import MovieCreator


def test_movie_creator__ok(mocker) -> None:
    mock_movie_repository = mocker.Mock()
    creator = MovieCreator(mock_movie_repository)

    with open("backend/tests/utils/data/file_example_MP4_1920_18MG.mp4", "rb") as f:
        data = f.read()

    creator.run(
        files=[{"name": "image.jpg", "data": data, "media_type": "image/jpeg"}],
        rating=4.5,
        metadata_={"title": "Title", "description": "Description"},
        channel_id="channel_id",
    )
