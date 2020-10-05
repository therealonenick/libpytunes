from six import iteritems


class Song:
    """
    Song Attributes:
    name (String)
    track_id (Integer)
    artist (String)
    album_artist (String)
    composer = None (String)
    album = None (String)
    genre = None (String)
    kind = None (String)
    size = None (Integer)
    total_time = None (Integer)
    track_number = None (Integer)
    track_count = None (Integer)
    disc_number = None (Integer)
    disc_count = None (Integer)
    year = None (Integer)
    date_modified = None (Time)
    date_added = None (Time)
    bit_rate = None (Integer)
    sample_rate = None (Integer)
    comments = None (String)
    rating = None (Integer)
    rating_computed = False (Boolean)
    album_rating = None (Integer)
    play_count = None (Integer)
    location = None (String)
    location_escaped = None (String)
    compilation = False (Boolean)
    grouping = None (String)
    lastplayed = None (Time)
    skip_count = None (Integer)
    skip_date = None (Time)
    length = None (Integer)
    persistent_id = None (String)
    album_rating_computed = False (Boolean)
    work = None (String)
    movement_name = None (String)
    movement_number = None (Integer)
    movement_count = None (Integer)
    playlist_only = None (Bool)
    apple_music = None (Bool)
    protected = None (Bool)
    purchased = None (Bool)
    play_epoch = None (Integer)
    track_type = None (String)
    file_folder_count = None (Integer)
    library_folder_count = None (Integer)
    release_date = None (Time)
    normalization = None (Integer)
    artwork_count = None (Integer)
    has_video = None (Bool)
    hd = None (Bool)
    video_width = None (Integer)
    video_height = None (Integer)
    music_video = None (Bool)
    bpm = None (Integer)
    sort_artist = None (String)
    sort_album = None (String)
    sort_name = None (String)
    explicit = None (Bool)
    movie = None (Bool)
    series = None (String)
    season = None (Integer)
    episode = None (String)
    episode_order = None (Integer)
    content_rating = None (String)
    tv_show = None (Bool)
    podcast = None (Bool)
    unplayed = None (Bool)
    clean = None (Bool)
    loved = None (Bool)
    """
    name = None
    track_id = None
    artist = None
    album_artist = None
    composer = None
    album = None
    genre = None
    kind = None
    size = None
    total_time = None
    track_number = None
    track_count = None
    disc_number = None
    disc_count = None
    year = None
    date_modified = None
    date_added = None
    bit_rate = None
    sample_rate = None
    comments = None
    rating = None
    rating_computed = None
    album_rating = None
    play_count = None
    skip_count = None
    skip_date = None
    location = None
    location_escaped = None
    compilation = None
    grouping = None
    lastplayed = None
    length = None
    persistent_id = None
    album_rating_computed = None
    work = None
    movement_name = None
    movement_number = None
    movement_count = None
    playlist_only = None
    apple_music = None
    protected = None
    purchased = None
    play_epoch = None
    track_type = None
    file_folder_count = None
    library_folder_count = None
    release_date = None
    normalization = None
    artwork_count = None
    has_video = None
    hd = None
    video_width = None
    video_height = None
    music_video = None
    bpm = None
    sort_artist = None
    sort_album = None
    sort_name = None
    explicit = None
    movie = None
    series = None
    season = None
    episode = None
    episode_order = None
    content_rating = None
    tv_show = None
    podcast = None
    unplayed = None
    sort_album_artist = None
    sort_composer = None
    clean = None
    loved = None


    def __iter__(self):
        for attr, value in iteritems(self.__dict__):
            yield attr, value

    def ToDict(self):
        return {key: value for (key, value) in self}
