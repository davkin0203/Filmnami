import React from 'react';

function Filter({ selectedFilter, onFilterChange }) {
    const handleFilterChange = (filter) => {
        onFilterChange(filter.target.value);
    };
  
  return (
    <div>
      <label className="custom-label">
        <span className="filter-text">Filter:</span>
        <select value={selectedFilter} onChange={handleFilterChange}>
          <option value="popular">Popular</option>
          <option value="top_rated">Top Rated</option>
        </select>
      </label>
    </div>
  );
}

export default Filter;