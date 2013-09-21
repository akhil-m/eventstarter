//
//  ESDetailViewController.h
//  Eventstarter
//
//  Created by Rohit Sanbhadti on 9/21/13.
//  Copyright (c) 2013 Eventstarter. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ESDetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;

@property (weak, nonatomic) IBOutlet UILabel *detailDescriptionLabel;
@end
