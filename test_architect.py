import unittest
from src.architect import generate_yaml, run_aws_architect_agent


class TestArchitect(unittest.TestCase):
    def test_generate_yaml(self):
        question = "Please design a simple S3 bucket architecture."
        yaml_content = generate_yaml(question)
        self.assertIn("AWS::S3::Bucket", yaml_content)

    def test_run_aws_architect_agent(self):
        question = "Please design an architecture that connects an EC2 instance to an RDS database."
        messages = run_aws_architect_agent(question)
        self.assertTrue(len(messages) > 1)
        self.assertIn("AWS::EC2::Instance", messages[-2].content)
        self.assertIn("AWS::RDS::DBInstance", messages[-2].content)

if __name__ == "__main__":
    unittest.main()


