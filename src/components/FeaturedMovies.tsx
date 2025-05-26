import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import MovieCard from './MovieCard';
import { useToast } from '@/hooks/use-toast';
import apiService from '@/services/api';

const featuredMovies = [
  {
    id: 1,
    title: "The Matrix Resurrections",
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
    rating: 8.7,
    year: 2021,
    duration: "148 min",
    genre: "Sci-Fi"
  },
  {
    id: 2,
    title: "Dune",
    poster: "https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
    rating: 9.2,
    year: 2021,
    duration: "155 min",
    genre: "Sci-Fi"
  },
  {
    id: 3,
    title: "No Time to Die",
    poster: "https://images.unsplash.com/photo-1489599904472-284d04d17f69?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
    rating: 8.4,
    year: 2021,
    duration: "163 min",
    genre: "Action"
  },
  {
    id: 4,
    title: "Spider-Man: No Way Home",
    poster: "https://images.unsplash.com/photo-1635863138275-d9864d3584dc?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
    rating: 9.0,
    year: 2021,
    duration: "148 min",
    genre: "Action"
  }
];

const FeaturedMovies = () => {
  const [movies, setMovies] = useState(featuredMovies);
  const [isLoading, setIsLoading] = useState(true);
  const { toast } = useToast();

  useEffect(() => {
    fetchFeaturedMovies();
  }, []);

  const fetchFeaturedMovies = async () => {
    try {
      const response = await apiService.getFeaturedMovies();
      if (response.status === 200 && Array.isArray(response.data)) {
        setMovies(response.data);
      }
    } catch (error) {
      console.log('Using fallback featured movies');
      // Keep using the static movies as fallback
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="py-16 px-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-12">
        <h2 className="text-4xl font-bold text-white">Featured Movies</h2>
        <Link to="/search" className="text-blue-400 hover:text-blue-300 transition-colors font-semibold">
          View All →
        </Link>
      </div>
      
      {isLoading ? (
        <div className="text-center text-white">Loading featured movies...</div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {movies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      )}
    </div>
  );
};

export default FeaturedMovies;
