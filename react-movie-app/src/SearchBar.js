import React, {useEffect, useState} from "react";
import axios from 'axios';

const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';

function SearchBar() {
    const[searchQuery, setSearchQuery] = useState('');
    const[searchResults, setSearchResults] = useState([]);

    const handleInputChange = (event) => {
        setSearchQuery(event.target.value)
    }

    const fetchSearchResults = async (query) => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/search', {
                params: {
                    query: query,
                    page: 1,
                }
            });

            const searchData = response.data;
            console.log(searchData);
            const movieData = JSON.parse(searchData.movies);


            const moviesData = movieData.map((movie) => ({
                id: movie.id,
                title: movie.title,
                poster_path: movie.poster_path
                // Include any other properties you need
            }));
            setSearchResults(moviesData);
        } catch(error) {
            console.error('Error fetching search results: ', error);
        }
    };

    useEffect(() => {
        if (searchQuery.trim() !== '') {
            fetchSearchResults(searchQuery);
        } else {
            setSearchResults([]);
        }
    }, [searchQuery]);

    const handleSearchResultSelect = (result) => {
        setSearchQuery(result.name);
      };    

    return (
    <div className="search-bar">
        <span className="search-text">Search:</span>
        <input
            type="text"
            value={searchQuery}
            onChange={handleInputChange}
            placeholder="Search movies..."
            className="search-input"
        />
        {searchResults.length > 0 && (
            <ul className="dropdown-menu">
                {searchResults.map((movie) => (
                <li key={movie.movie_id} className='dropdown-item'>
                    <img src={`${BASE_URL}${movie.poster_path}`} alt={movie.title} />
                    <h2>{movie.title}</h2>
                </li>
            ))}
        </ul>
        )}
    </div>
    );
}
    
export default SearchBar;