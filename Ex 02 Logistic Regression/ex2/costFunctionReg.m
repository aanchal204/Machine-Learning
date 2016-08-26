function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

hypothesis = sigmoid(X*theta);
cost = -y.*log(hypothesis) - (1-y).*(log(1.-hypothesis));
J = 1.0/m * sum(cost);
theta_sq = theta.^2;
J = J + lambda*(sum(theta_sq)-theta_sq(1))/(2.0*m);

grad = 1.0/m*sum((hypothesis - y).*X) + lambda/m*theta';
grad(1) = grad(1) - lambda/m*theta'(1);



% =============================================================

end
