import React, { useEffect, useState } from 'react';
import Filter from './Filter';
import SearchBar from './SearchBar';
import PageNav from './PageNav';
import axios from 'axios';
import { Link } from 'react-router-dom';

function ListMovies() {
  const [movies, setMovies] = useState([]);
  const [selectedFilter, setSelectedFilter] = useState('popular');
  const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    // Fetch movies from your Django backend
    fetchMovies(selectedFilter, currentPage);
  }, [selectedFilter]);

  const fetchMovies = async (type, page) => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/home/movies/specified-movies/', {
          params: {
              type: type,
              page: page,
          }
      });

      const searchData = response.data;
      const movieData = JSON.parse(searchData.movies);

      const moviesData = movieData.map((movie) => ({
        movie_id: movie.movie_id,
        title: movie.title,
        poster_path: movie.poster_path,
      }));
      setMovies(moviesData);
      } catch(error) {
        console.error('Error fetching search results: ', error);
      }
    };

    const handleFilterChange = (filter) => {
      setSelectedFilter(filter);
      setCurrentPage(1);
    };

    const handlePageChange = (page) => {
      setCurrentPage(page);
      fetchMovies(selectedFilter, page);
    };

    return (
      <div className='list-movies'>
        <div className='site-header'>
          <h1>Filmnami</h1>
        </div>
        <div className='grid-container-filter-search'>
          <div className='grid-child filter'>
            <Filter selectedFilter={selectedFilter} onFilterChange={handleFilterChange}/>
          </div>
          <div className='grid-child search'>
            <SearchBar/>
          </div>
        </div>
        <div className='grid-container'>
          {movies.map((movie) => (
            <Link key={movie.movie_id} to={`/movies/${movie.movie_id}`}>
              <div className='grid-item'>
              {movie.poster_path ? (
                <img src={`${BASE_URL}${movie.poster_path}`} alt={movie.title} />
              ) : (
                <img
                  src="https://content.schoolinsites.com/api/documents/ebbca81b01694c91aa908f5374842a9f.gif"
                  alt={movie.title}
                />
              )}
              <h2>{movie.title}</h2>
              </div>
            </Link>
          ))}
        </div> 
        <PageNav currentPage={currentPage} onPageChange={handlePageChange}/>
      </div>
    );
  }
  
  export default ListMovies;