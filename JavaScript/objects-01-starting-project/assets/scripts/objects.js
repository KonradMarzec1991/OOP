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
        // const { title: movieTitle } = info;
        let { getFormattedTitle } = movie;
        // getFormattedTitle = getFormattedTitle.bind(movie);
        let text = getFormattedTitle.call(movie) + '-';
        for (let key in info) {
            if (key !== "title") {
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
        title.trim() === "" ||
        extraName.trim() === "" ||
        extraValue.trim() === ""
    ) {
        return;
    }

    const newMovie = {
        info: {
            title,
            [extraName]: extraValue
        },
        id: Math.random().toString(),
        getFormattedTitle() {
            return this.info.title.toUpperCase()
        }
    }
    movies.push(newMovie);
    renderMovies();
    console.log(newMovie);
};

const searchMovieHandler = () => {
    const filterTerm = document.getElementById("filter-title").value;
    renderMovies(filterTerm);
}

addMovieBtn.addEventListener("click", addMovieHandler);
searchBtn.addEventListener("click", searchMovieHandler);