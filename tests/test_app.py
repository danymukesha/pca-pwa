import unittest
from unittest.mock import patch, Mock, mock_open
from flask import Flask
from pca_pwa import app,  __version__

def test_verion():
	assert __version__ == '1.0.4'
    
class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.app.test_client()
        self.app.testing = True
    
    def tearDown(self):
        pass

    def test_index_route(self):
        # Test the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('pca_pwa.app.PCA')
    @patch('pca_pwa.app.SimpleImputer')
    def test_perform_pca_route(self, mock_imputer, mock_pca):
        # Mock the file upload and imputer
        mock_file = Mock()
        mock_file.filename = 'samples_file.xlsx'

        mock_imputer_instance = mock_imputer.return_value
        mock_pca_instance = mock_pca.return_value

        mock_imputer_instance.fit_transform.return_value = [[1, 2], [3, 4]]
        mock_pca_instance.fit_transform.return_value = [[0.1, 0.2], [0.3, 0.4]]

        with patch('builtins.open', mock_open(read_data='test data')):
            with patch('pca_pwa.app.os.path.exists', return_value=False):
                with patch('pca_pwa.app.os.makedirs'):
                    response = self.app.post('/perform_pca', data={'file': str(mock_file), 'imputation_method': 'mean'})

        self.assertEqual(response.status_code, 200)
        # Add more assertions based on other expected behavior

    def test_save_results_to_folder(self):        
		# Extract data from the DataFrame
        original_data = [["A", 1, 2], ["B", 3, 4]]
        header = [row[0] for row in original_data]
        data_array = [row[1:] for row in original_data]
        
        pca = app.PCA(n_components=2)
        transformed_data = pca.fit_transform(data_array)
        base64_image_string = app.plot_pca(transformed_data, header, pca)
        
        # Mock the result and folder path
        result = {
            'original_data': [[1, 2], [3, 4]],
            'transformed_data': transformed_data,
            'header': ['A', 'B'],
            'plot_image': base64_image_string,
            'imputation_warning': 'mean'
        }
        folder_path = 'test_folder'

        # Create a temporary directory for testing
        with unittest.mock.patch('tempfile.mkdtemp') as mock_mkdtemp:
            mock_mkdtemp.return_value = folder_path
            app.save_results_to_folder(result, folder_path)

        # Add assertions based on other expected behavior

if __name__ == '__main__':
    unittest.main()
