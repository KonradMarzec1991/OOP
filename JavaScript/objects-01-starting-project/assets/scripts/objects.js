const addMovieBtn = document.getElementById("add-movie-btn");
const searchBtn = document.getElementById("search-btn");

const movies = [];

const renderMovies = (filterName = "") => {
    const movieList = document.getElementById("movie-list");
    if (movies.length === 0) {
        movieList.classList.remove("visible");
    } else {
        movieList.classList.add("visible");
    }
    movieList.innerHTML = "";

    const filterMovies = !filterName
    ? movies
    : movies.filter(movie => movie.info.title.includes(filterName));

    filterMovies.forEach((movie) => {
        const movieEl = document.createElement("li");
        const { info, ...otherProps } = movie;

        let { getFormattedTitle } = movie;
        let text = getFormattedTitle.call(movie) + '-';

        for (let key in info) {
            if (key !== "title" && key !== "_title") {
                text += `${key}: ${info[key]}`
            }
        }
        movieEl.textContent = text;
        movieList.append(movieEl);
    })
};

const addMovieHandler = () => {
    const title = document.getElementById("title").value;
    const extraName = document.getElementById("extra-name").value;
    const extraValue = document.getElementById("extra-value").value;

    if (
        extraName.trim() === "" ||
        extraValue.trim() === ""
    ) {
        return;
    }

    const newMovie = {
        info: {
            set title(val) {
                if (val.trim() === "") {
                    this._title = "DEFAULT";
                } else {
                    this._title = val;
                }
            },
            get title() {
                return this._title.toUpperCase();
            },
            [extraName]: extraValue
        },
        id: Math.random().toString(),
    }

    newMovie.info.title = title;

    movies.push(newMovie);
    renderMovies();
};

const searchMovieHandler = () => {
    const filterTerm = document.getElementById("filter-title").value;
    renderMovies(filterTerm);
}

addMovieBtn.addEventListener("click", addMovieHandler);
searchBtn.addEventListener("click", searchMovieHandler);