import './App.css';
import MovieList from './MovieList';

function App() {
  return (
    <div className="movie-list">
      <div className='site-header'>
        <h1>Movies</h1>
      </div>
      <MovieList/>
    </div>
  );
}

export default App;
