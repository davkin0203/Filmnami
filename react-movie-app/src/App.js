import './App.css';
import MovieList from './MovieList';

function App() {
  return (
    <div className="movie-list">
      <div className='site-header'>
        <h1>Popular Movies This Week!</h1>
      </div>
      <MovieList/>
    </div>
  );
}

export default App;
