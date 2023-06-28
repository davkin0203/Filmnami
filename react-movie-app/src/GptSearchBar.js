import React, {useEffect, useState} from "react";
import axios from 'axios';

const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';

function GptSearchBar() {
    const[searchInput, setSearchInput] = useState('');
    const[searchResults, setSearchResults] = useState([]);

    const handleInputChange = (event) => {
        setSearchInput(event.target.value);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            fetchSearchResults(searchInput);
        }
    };

    const handleButtonClick = () => {
        fetchSearchResults(searchInput);
    };

    const fetchSearchResults = async (input) => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/home/movies/search-gpt', {
                params: {
                    input: input,
                }
            });

            const searchData = response.data;
            const movieData = JSON.parse(searchData.movies);

            const moviesData = movieData.map((movie) => ({
                movie_id: movie.id,
                title: movie.title,
                poster_path: movie.poster_path
                // Include any other properties you need
            }));
            setSearchResults(moviesData);
        } catch(error) {
            console.error('Error fetching search results: ', error);
        }
    };

    const handleSearchResultSelect = (result) => {
        setSearchInput(result.name);
      };    

    return (
    <div className="search-bar">
        <span className="search-text">Search(GPT):</span>
        <input
            type="text"
            value={searchInput}
            onChange={handleInputChange}
            onKeyDown={handleKeyDown}
            placeholder="Ask ChatGPT..."
            className="search-input"
        />
        <button onClick={handleButtonClick}>Enter</button>
        {searchResults.length > 0 && (
            <ul className="dropdown-menu-gpt">
                {searchResults.map((movie) => (
                <li key={movie.movie_id} className='dropdown-item'>
                    {movie.poster_path !== null && <img src={`${BASE_URL}${movie.poster_path}`} alt={movie.title} />}
                    {movie.poster_path === null && <img src={'https://content.schoolinsites.com/api/documents/ebbca81b01694c91aa908f5374842a9f.gif'} alt={movie.title} />}
                    <h2>{movie.title}</h2>
                </li>
            ))}
        </ul>
        )}
    </div>
    );
}
    
export default GptSearchBar;