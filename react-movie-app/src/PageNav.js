import React from "react";

function PageNav({ currentPage, onPageChange }) {
    const handlePageChange = (event) => {
        onPageChange(event.target.value);
    }

    return (
        <div>
            <label className="page-nav">
                <span className="page-text">
                    <select value={currentPage} onChange={handlePageChange}>
                        <option>
                            1
                        </option>
                        <option>
                            2
                        </option>
                        <option>
                            3
                        </option>
                    </select>
                </span>
            </label>
        </div>
    )
}

export default PageNav;