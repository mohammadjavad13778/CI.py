import yaml

# Define your CI/CD pipeline structure
pipeline_config = {
    'stages': ['build', 'test', 'deploy'],
    'jobs': {
        'build':
            {
                'stage': 'build',
                'script': ['echo "Building..."']
            },
        'test':
            {
                'stage': 'test',
                'script': ['echo "Testing..."']
            },
        'deploy':
            {
                'stage': 'deploy',
                'script': ['echo "Deploying..."']
            }
    }
}

# Convert the Python structure to YAML
yaml_content = yaml.dump(pipeline_config)

# Write the YAML to .gitlab-ci.yml file
with open('.gitlab-ci.yml', 'w') as yaml_file:
    yaml_file.write(yaml_content)

print("GitLab CI/CD configuration generated successfully.")

