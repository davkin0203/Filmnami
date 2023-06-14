import React from 'react';

function Filter({ selectedFilter, onFilterChange }) {
  return (
    <div>
      <label className="custom-label">
        <span className="filter-text">Filter:</span>
        <select value={selectedFilter} onChange={(event) => onFilterChange(event.target.value)}>
          <option value="popular">Popular</option>
          <option value="old">Old</option>
        </select>
      </label>
    </div>
  );
}

export default Filter;