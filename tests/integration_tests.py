import subprocess
import pytest

# Helper function to run the command and capture output
def run_command(args):
    """Helper function to run the geoloc-util command and return the output."""
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode

# Test for valid city/state input
def test_valid_city_state():
    """Test the utility with a valid city/state input."""
    args = ['python', 'geoloc_util.py', '--locations', 'Madison, WI']
    stdout, stderr, exit_code = run_command(args)
    
    assert exit_code == 0
    assert 'Madison' in stdout
    assert 'lat' in stdout
    assert 'lon' in stdout

# Test for valid ZIP code input
def test_valid_zip_code():
    """Test the utility with a valid ZIP code input."""
    args = ['python', 'geoloc_util.py', '--locations', '90210']
    stdout, stderr, exit_code = run_command(args)
    
    assert exit_code == 0
    assert 'Beverly Hills' in stdout
    assert 'lat' in stdout
    assert 'lon' in stdout

# Test for multiple valid locations
def test_multiple_locations():
    """Test the utility with multiple valid inputs (city/state and ZIP codes)."""
    args = ['python', 'geoloc_util.py', '--locations', 'Madison, WI', '90210', 'New York, NY']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    assert 'Madison' in stdout
    assert 'Beverly Hills' in stdout
    assert 'New York County' in stdout

# Test for an invalid location
def test_invalid_location():
    """Test the utility with an invalid location."""
    args = ['python', 'geoloc_util.py', '--locations', 'Fake City, ZZ']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    assert 'No data found for location' in stdout

# Test for missing input
def test_missing_input():
    """Test the utility without providing any location."""
    args = ['python', 'geoloc_util.py']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code != 0
    assert 'usage' in stderr  # Expect a usage/help message when no arguments are provided

# Test for multiple ZIP code inputs
def test_multiple_zip_codes():
    """Test the utility with multiple ZIP codes."""
    args = ['python', 'geoloc_util.py', '--locations', '90210', '10001']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    assert 'Beverly Hills' in stdout
    assert 'New York' in stdout

# Test for city name that exists in multiple states
def test_city_with_multiple_states():
    """Test the utility with a city name that exists in multiple states (Springfield)."""
    args = ['python', 'geoloc_util.py', '--locations', 'Springfield, IL']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    assert 'Springfield' in stdout
    assert 'Illinois' in stdout

# Test for empty location input
def test_empty_location_input():
    """Test the utility with an empty string as location input."""
    args = ['python', 'geoloc_util.py', '--locations', '']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    assert 'Invalid city/state input format' in stdout

# Test for location with special characters
def test_location_with_special_characters():
    """Test the utility with a location that has special characters (St. Louis, MO)."""
    args = ['python', 'geoloc_util.py', '--locations', 'St. Louis, MO']
    stdout, stderr, exit_code = run_command(args)

    assert exit_code == 0
    # Allow for "Saint Louis" as a valid return since the API uses this format
    assert 'Saint Louis' in stdout or 'St. Louis' in stdout
    assert 'lat' in stdout
    assert 'lon' in stdout